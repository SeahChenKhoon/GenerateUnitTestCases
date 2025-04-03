from theory_evaluation.utils import (
    validate_user,
    get_marking_scheme,
    manage_user_performance,
    get_user_performance,
    delete_user_performance,
)

# Third party packages
import time
import logging
import json
import pydantic
from uuid import UUID
from typing import Optional
from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import StreamingResponse

# Intrinsic packages
import asyncio
from theory_evaluation.llm_handler import OpenAI_llm
from theory_evaluation.llm_utils import initialise_prompt, initialise_settings


router = APIRouter()
llm_completion = OpenAI_llm(useAzureOpenAI=True, output="json", verbose=False)


async def process_theory_evaluation(
    email: pydantic.EmailStr,
    question_id: UUID,
    answer: str,
    question: str,
    marking_scheme: str,
    model_answer: str,
):
    # Generate evaluation and scoring ==================================
    try:
        prompt_message = initialise_prompt(agent="evaluation")
        prompt_message = prompt_message.replace("{$question}", question)
        prompt_message = prompt_message.replace("{$answer}", answer)
        prompt_message = prompt_message.replace("{$marking_scheme}", marking_scheme)
        prompt_message = prompt_message.replace("{$model_answer}", model_answer)
        llm_completion.message = prompt_message
        llm_completion.config = initialise_settings(agent="evaluation")

        # Parse the concatenated JSON string
        response_content = []
        async for chunk in llm_completion.execute():
            if isinstance(chunk, dict):
                chunk = json.dumps(chunk)
            response_content.append(chunk)

        response_text = "".join(response_content)
        response_data = json.loads(response_text)

        theory_evaluation = response_data.get("Evaluation")
        score = response_data.get("Score")
        grade = response_data.get("Grade")

        if theory_evaluation is not None and score is not None and grade is not None:
            # Update user performance score  ==============================
            attempt_allowed = manage_user_performance(
                mode=1,
                email=email,
                question_id=question_id,
                llm_evaluation=theory_evaluation,
                llm_score=score,
                user_grade=grade,
            )
            if not attempt_allowed:
                print("Unable to update user's performance.")
                return
        else:
            _ = manage_user_performance(mode=2, email=email, question_id=question_id)
            print("Error in LLM response format.")
            return

    except Exception as e:
        print(f"Unexpected error encountered: {e}.")
        _ = manage_user_performance(mode=2, email=email, question_id=question_id)

    # score_match = re.search(r"Final Score:\s*(\d+)", str(theory_result))
    # if score_match:
    # final_score = int(score_match.group(1))

    # evaluation_match = re.search(
    #     r"Evaluation:(.*?)Final Score:", str(theory_result), re.DOTALL
    # )
    # if evaluation_match:
    #     theory_evaluation = evaluation_match.group(1).strip()

    #     # Update user performance score  ==============================
    #     attempt_allowed = manage_user_performance(
    #         edx_user_id,
    #         email,
    #         question,
    #         1,
    #         llm_evaluation=theory_evaluation,
    #         llm_score=final_score,
    #     )
    #     if not attempt_allowed:
    #         return  # Future error logging somewhere

    #     if environment != "local":
    #         # Get access token for OpenEDX update =========================
    #         access_token = request_access_token()
    #         if not access_token:
    #             print("OpenEDX scoring not updated.")
    #             return  # Future error logging somewhere

    #         # Create csv file for post back ===============================
    #         update_openedx(access_token, edx_user_id, email, block_id, final_score)

    # else:
    #     _ = manage_user_performance(edx_user_id, email, question, 2)
    #     print("Evaluation regex fails.")
    #     return  # Future error logging somewhere
    # else:
    #     _ = manage_user_performance(edx_user_id, email, question, 2)
    #     print("Score regex fails.")
    #     return  # Future error logging somewhere


## API schema for Theory Evaluation - POST request
class EvaluateTheoryPOSTRequest(pydantic.BaseModel):
    """
    Represents the data structure for a request to evaluate a student's answer based on a theoretical question.
    Used to parse and validate incoming data for the theory evaluation API.

    Attributes:
    - email (str): unique id of the student for identification.
    - uuid (UUID): The uuid to identify the theoretical question answered.
    - answer (str): The student's proposed answer to the question.
    """

    email: pydantic.EmailStr
    uuid: UUID
    answer: str


logger = logging.getLogger(__name__)


## POST API for theory evaluation
@router.post("/api/v1/evaluate-theory")
async def evaluate_theory(
    background_tasks: BackgroundTasks, response: EvaluateTheoryPOSTRequest
):
    """
    Evaluate a student's answer based the given thereotical question.

    This endpoint takes a theory evaluation request and returns the LLM's evaluation results and scoring, including errors.

    Args:
    - response (EvaluateTheoryRequest): Request object containing the user-id, the thereotical question attempted and the student's answer.

    Returns:
    - status and status message of POST request
    """
    start_time = time.time()
    if not response.email or not response.uuid or not response.answer:
        raise HTTPException(
            status_code=400, detail="Missing email, question's uuid or user's answers."
        )

    # Query for existence of student and corresponding marking scheme and model answer from the `curriculum` data table
    user_existence = validate_user(response.email)
    question, marking_scheme, model_answer = get_marking_scheme(response.uuid)

    if not user_existence:
        return {
            "status": "Not Accepted",
            "message": "User's email does not exist.",
        }
    elif not (question, marking_scheme and model_answer):
        return {
            "status": "Not Accepted",
            "message": "Question does not exist. No marking scheme and model answer found.",
        }
    else:
        # first check user_attempts and create one attempt row in the table
        manage_start_time = time.time()
        attempt_allowed = manage_user_performance(
            mode=0,
            email=response.email,
            question_id=response.uuid,
            user_response=response.answer,
        )
        manage_end_time = time.time()
        logger.info(
            f"manage_user_performance execution time: {manage_end_time - manage_start_time} seconds"
        )

        if not attempt_allowed:
            return {
                "status": "Not Accepted",
                "message": "User's number of attempts exceeded the limit.",
            }
        background_start_time = time.time()
        background_tasks.add_task(
            process_theory_evaluation,
            response.email,
            response.uuid,
            response.answer,
            question,
            marking_scheme,
            model_answer,
        )
        background_end_time = time.time()
        logger.info(
            f"Adding background task execution time: {background_end_time - background_start_time} seconds"
        )

        end_time = time.time()
        logger.info(
            f"Total evaluate_theory execution time: {end_time - start_time} seconds"
        )

        return {"status": "Accepted", "message": "Processing started"}


class TheoryEvaluationScoreRequest(pydantic.BaseModel):
    """
    Represents the data structure for a request to get LLM's evaluation and grading for student answer.
    Used to parse and validate incoming data for the theory evaluation score request API.

    Attributes:
    - email (str): unique id of the student for identification.
    - uuid (UUID): The uuid to identify the theoretical question answered.
    """

    email: pydantic.EmailStr
    uuid: UUID


## POST API for theory evaluation's score
@router.post("/api/v1/get-theory-score")
async def get_theory_score(response: TheoryEvaluationScoreRequest):
    if not response.email or not response.uuid:
        raise HTTPException(status_code=400, detail="Missing email or question")

    # Query for existence of student and corresponding marking scheme from the `curriculum` datatable =========================
    user_existence = validate_user(response.email)
    question, marking_scheme, model_answer = get_marking_scheme(response.uuid)

    if not user_existence or not (question, marking_scheme and model_answer):
        return {
            "user_attempts": 0,
            "evaluation": "No evaluation available.",
            "grade": "No grade available.",
        }

    # Initialise with default value
    user_attempts, llm_evaluation, user_grade, llm_evaluation_status = (
        0,
        "LLM evaluation process is still ongoing. Please wait.",
        "No grade available.",
        1,
    )
    # llm_evaluation_status == 1, llm evaluation still pending.
    # llm_evaluation_status == 2, evaluation completed successfully.
    # llm_evaluation_status == 0, error occurs.
    while (
        llm_evaluation_status == 1
    ):  # If llm_status is pending, loop till evaluation comes back
        user_attempts, llm_evaluation, user_grade, llm_evaluation_status = (
            get_user_performance(response.email, response.uuid)
        )
        if llm_evaluation_status == 0 or llm_evaluation_status == 2:
            break
        await asyncio.sleep(0.2)

    # Check if user_attempts is 3 and append model_answer to llm_evaluation
    if user_attempts == 3:
        llm_evaluation += "\n\n" + f"Model Answer: {model_answer}"

    return {
        "user_attempts": user_attempts,
        "evaluation": llm_evaluation,
        "grade": user_grade,
    }


class TheoryEvaluationDeleteRequest(pydantic.BaseModel):
    """
    Represents the data structure for a request to delete LLM's evaluation and grading for student answer.
    Used to parse and validate incoming data for the theory evaluation score request API.

    Attributes:
    - email (str): unique id of the student for identification.
    - uuid (UUID): The uuid to identify the theoretical question answered.
    """

    email: pydantic.EmailStr
    uuid: Optional[UUID] = UUID("00000000-0000-0000-0000-000000000000")


## POST API to delete user evaluation's score
@router.post("/api/v1/delete-theory-score", status_code=204)
def delete_theory_score(response: TheoryEvaluationDeleteRequest):
    if not response.email:
        raise HTTPException(status_code=400, detail="Missing email")

    user_existence = validate_user(response.email)
    if not user_existence:
        raise HTTPException(status_code=404, detail="Missing user")

    deleted = delete_user_performance(response.email, response.uuid)

    if not deleted:
        raise HTTPException(status_code=400, detail="Error querying database")
    return
