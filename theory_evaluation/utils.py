import os
import time
import pydantic
from uuid import UUID

# import re
# import csv
# from datetime import datetime
# from collections import Counter

# ORM for database querying
from sqlalchemy import create_engine, and_, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from contextlib import contextmanager

# Libraries for postgres database
from theory_evaluation import models

SessionLocal = None  # Global session factory

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
ssl_mode = os.getenv("SSL_MODE")
environment = os.getenv("ENVIRONMENT", "local")

if environment == "local":
    conn_str = f"postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
else:
    conn_str = (
        f"postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/"
        f"{db_name}?sslmode={ssl_mode}"
    )

engine = create_engine(conn_str)
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


def init_db_session():
    """
    Initializes the SQLAlchemy session factory using environment variables.
    """
    global SessionLocal

    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    ssl_mode = os.getenv("SSL_MODE")
    environment = os.getenv("ENVIRONMENT", "local")

    if environment == "local":
        conn_str = f"postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    else:
        conn_str = (
            f"postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/"
            f"{db_name}?sslmode={ssl_mode}"
        )

    engine = create_engine(conn_str)
    SessionLocal = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )

@contextmanager
def get_db():
    """
    Establishes a database session using SQLAlchemy ORM.

    This function creates a new session with the database defined by the environment variables DB_USER, DB_PASSWORD, DB_NAME, DB_HOST, and DB_PORT. The session is created with autocommit and autoflush set to False, meaning changes won't be automatically committed to the database and queries won't be automatically flushed.

    The function uses a context manager to ensure that the session is properly closed after use, even if an error occurs. This is done using a try-finally block.

    Parameters:
    None

    Returns:
    - db (scoped_session): A SQLAlchemy session object that can be used to interact with the database. This object is yielded, meaning it can be used in a with statement to ensure it's properly closed after use.

    Raises:
    - SQLAlchemyError: An error from SQLAlchemy if there's a problem establishing a connection to the database.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


### Validate user email from user_info table
def validate_user(email):
    """
    To check if the user exist and valid for the course.

    Args:
        email (pydantic.EmailStr): The email of the student to be validated.

    Returns:
        user_existent (Boolean or None): True if a user with the given email and a status of 1 exists, otherwise False. None if error occurs.
    """
    # Use the provided get_db generator for the session management
    try:
        with get_db() as db:
            user = (
                db.query(models.UserInfo)
                .filter(
                    and_(models.UserInfo.email == email, models.UserInfo.status == 1)
                )
                .first()
            )
            # Return True if the user exists (user is not None), otherwise False
            user_existence = user is not None
        return user_existence

    except OperationalError as e:
        print(f"OperationalError encountered: {e}. Connection issues may be present.")
        return None

    except SQLAlchemyError as e:
        print(f"SQLAlchemyError encountered: {e}. Error executing query.")
        return None

    except Exception as e:
        print(f"Unexpected error encountered: {e}.")
        return None


### Get marking scheme to corresponding question based on uuid
def get_marking_scheme(uuid):
    try:
        with get_db() as db:
            curriculum = (
                db.query(models.Curriculum).filter(models.Curriculum.id == uuid).first()
            )
        return curriculum.question, curriculum.marking_scheme, curriculum.model_answer

    except OperationalError as e:
        print(f"OperationalError encountered: {e}. Connection issues may be present.")
    except SQLAlchemyError as e:
        print(f"SQLAlchemyError encountered: {e}. Error executing query.")
    except Exception as e:
        print(f"Unexpected error encountered: {e}.")

    return None, None, None


# def request_access_token():
#     url = os.getenv(
#         "OPENEDX_ACCESSTOKEN_URL"
#     )  # "https://dev.juruku.ai/oauth2/access_token"
#     grant_type = os.getenv("OPENEDX_GRANT_TYPE")  # "password"
#     username = os.getenv("OPENEDX_USERNAME")  # "ruth"
#     password = os.getenv("OPENEDX_PASSWORD")  # "edx"
#     token_type = os.getenv("OPENEDX_TOKEN_TYPE")  # "JWT"
#     client_id = os.getenv("OPENEDX_CLIENT_ID")  # "login-service-client-id"

#     # Define the payload
#     payload = {
#         "grant_type": grant_type,
#         "username": username,
#         "password": password,
#         "token_type": token_type,
#         "client_id": client_id,
#     }

#     try:
#         # Send the POST request
#         response = requests.post(url, data=payload)

#         # Check the response status code
#         if response.status_code == 200:
#             return response.json().get("access_token")
#         else:
#             print("Request access token failed.")
#             return None

#     except ConnectionError:
#         print(
#             "Failed to connect to the access token URL. Please check the URL and your network connection."
#         )
#         return None
#     except RequestException as e:
#         print(f"An error occurred while requesting the access token: {e}")
#         return None
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         return None


# def update_openedx(
#     access_token,
#     edx_user_id,
#     email,
#     block_id,
#     final_score,
#     full_name=None,
#     student_uid=None,
#     enrolled=None,
#     track=None,
#     cohort=None,
#     title=None,
#     date_last_graded=None,
#     who_last_graded=None,
#     PreviousPoints=None,
# ):

#     # File not existent
#     # Define the CSV file path
#     # script_dir = os.path.dirname(os.path.abspath(__file__)) #locall
#     # file_path = os.path.join(script_dir, "data", "user_performance.csv") #locall

#     # Generate a timestamp in a suitable format (e.g., YYYYMMDD_HHMMSS)
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     file_path = f"/tmp/user_performance_{email}_{timestamp}.csv"
#     try:
#         with open(file_path, "x", newline="") as csvfile:  # Attempt to create file
#             writer = csv.writer(csvfile)

#             # Write headers if file is new
#             writer.writerow(
#                 [
#                     "user_id",
#                     "user_name",
#                     "full_name",
#                     "student_uid",
#                     "enrolled",
#                     "track",
#                     "cohort",
#                     "block_id",
#                     "title",
#                     "date_last_graded",
#                     "who_last_graded",
#                     "Previous Points",
#                     "New Points",
#                 ]
#             )

#     except FileExistsError:
#         pass

#     block_id_csv = (
#         f"block-v1:AISG+AIABC+2024-H2+type@staffgradedxblock+block@{block_id}"
#     )
#     # Open the file in append mode to add new data
#     with open(file_path, "a", newline="") as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(
#             [
#                 edx_user_id,
#                 email,
#                 full_name,
#                 student_uid,
#                 enrolled,
#                 track,
#                 cohort,
#                 block_id_csv,
#                 title,
#                 date_last_graded,
#                 who_last_graded,
#                 PreviousPoints,
#                 final_score,
#             ]
#         )

#     # Send the file to the API
#     try:
#         openedx_url = os.getenv("OPENEDX_URL")
#         url = f"{openedx_url}/courses/course-v1:AISG+AIABC+2024-H2/xblock/block-v1:AISG+AIABC+2024-H2+type@staffgradedxblock+block@{block_id}/handler/csv_import_handler"
#         payload = {}
#         files = [
#             (
#                 "csv",
#                 (
#                     f"user_performance_{email}_{timestamp}.csv",
#                     open(file_path, "rb"),
#                     "text/csv",
#                 ),
#             )
#         ]
#         headers = {
#             "Authorization": f"JWT {access_token}",
#             "Cache-Control": "no-cache",
#         }

#         response = requests.request(
#             "POST", url, headers=headers, data=payload, files=files
#         )
#         response.raise_for_status()

#     except RequestException as e:
#         print(f"Request failed: {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#     finally:
#         os.remove(file_path)
#         print(f"File {file_path} has been removed.")


def get_user_performance(
    email: pydantic.EmailStr,
    question_id: UUID,
    max_retries: int = 3,
    retry_delay: int = 2,
):
    """
    Retrieve the user's performance based on their email and question.

    Parameters:
    - email (pydantic.EmailStr): The user's email.
    - question_id (UUID): The specific question's uuid.
    - max_retries (int): Maximum number of retries for the operation due to OperationalError.
    - retry_delay (int): Delay between retries in seconds.

    Returns:
    Tuple[int, str, str, int]: A tuple containing the number of attempts, the LLM evaluation, LLM grading and the status of the LLM evaluation.
    """
    # Initialize default values in case of no data or an error
    default_response = (
        0,
        "An unexpected error occurred. Please try again.",
        "No grade available.",
        0,
    )
    retries = 0

    while retries < max_retries:
        try:
            with get_db() as db:
                # Retrieve the user performance record from the database
                user_performance = (
                    db.query(models.TheoryEvalUserPerformance)
                    .filter(
                        and_(
                            models.TheoryEvalUserPerformance.email == email,
                            models.TheoryEvalUserPerformance.question_id == question_id,
                        )
                    )
                    .order_by(desc(models.TheoryEvalUserPerformance.timestamp))
                    .first()
                )

                if user_performance:
                    return (
                        user_performance.user_attempts,
                        user_performance.llm_evaluation,
                        user_performance.user_grade,
                        user_performance.llm_evaluation_status,
                    )
                else:
                    return default_response

        except OperationalError as e:
            print(f"OperationalError: {e}. Retrying...")
            retries += 1
            time.sleep(retry_delay)

        except SQLAlchemyError as e:
            print("Error querying database:", e)
            return default_response

    # Return default response if retries are exhausted without success
    if retries == max_retries:
        print("Maximum retries reached. Returning default response.")
        return default_response


# =========================================================================================
def manage_user_performance(
    mode: input,
    email: pydantic.EmailStr,
    question_id: UUID,
    user_response: str | None = None,
    llm_evaluation: str | None = None,
    llm_score: int | None = None,
    user_grade: str | None = None,
    max_retries: int = 3,
    retry_delay: int = 2,
):
    """
    Manage user performance based on the mode.
    Mode 0: Creates a new attempt.
    Mode 1: Updates llm_evaluation, llm_score and user_grade.
    Mode 2: Decreases user attempts logged previously when error from LLM occurs.

    Parameters:
    - mode (int): Operation mode (0: new attempt, 1: update performance, 2: decrement attempts).
    - email (pydantic.EmailStr): User's email.
    - question_id (UUID): The question's uuid attempted by the user.
    - user_response (str, optional): User's response to the question. Required for mode 0.
    - llm_evaluation (str, optional): LLM's evaluation of the user's response. Required for mode 1.
    - llm_score (int, optional): Score given by LLM based on user's response. Required for mode 1.
    - user_grade (str, optional): Pass or Fail based on the score band.
    - max_retries (int): For controlling the retries attempt to access the db whenever there is db connection issue
    - retry_delay (int): Seconds of delay before retries.

    Returns:
    - attempt_allowed (boolean)
    """
    retries = 0
    while retries < max_retries:
        try:
            with get_db() as db:
                # To create new row for new attempts - if attempts == 3 and evaluated by llm, return/ if latest attempt has no evaluation, previous llm evaluation has error and update the table/ if attempt < 3, update table.
                if mode == 0:
                    user_performance = (
                        db.query(models.TheoryEvalUserPerformance)
                        .filter(
                            and_(
                                models.TheoryEvalUserPerformance.email == email,
                                models.TheoryEvalUserPerformance.question_id
                                == question_id,
                            )
                        )
                        .order_by(models.TheoryEvalUserPerformance.timestamp.desc())
                        .first()
                    )

                    if user_performance:  # user attempted question
                        if (
                            user_performance.user_attempts == 3
                            and user_performance.llm_evaluation
                        ):
                            print("User has reached the maximum attempt limit.")
                            return False
                        else:
                            db.add(
                                models.TheoryEvalUserPerformance(
                                    email=email,
                                    question_id=question_id,
                                    user_response=user_response,
                                    user_attempts=user_performance.user_attempts + 1,
                                    llm_evaluation_status=1,
                                )
                            )
                    else:  # first attempt of question
                        db.add(
                            models.TheoryEvalUserPerformance(
                                email=email,
                                question_id=question_id,
                                user_response=user_response,
                                user_attempts=1,
                                llm_evaluation_status=1,
                            )
                        )

                # To update with llm evaluation and scoring
                elif mode == 1:
                    user_performance = (
                        db.query(models.TheoryEvalUserPerformance)
                        .filter(
                            and_(
                                models.TheoryEvalUserPerformance.email == email,
                                models.TheoryEvalUserPerformance.question_id
                                == question_id,
                            )
                        )
                        .order_by(models.TheoryEvalUserPerformance.timestamp.desc())
                        .first()
                    )
                    if user_performance:
                        user_performance.llm_evaluation = llm_evaluation
                        user_performance.llm_score = llm_score
                        user_performance.user_grade = user_grade
                        user_performance.llm_evaluation_status = 2

                # Occurs when llm has error and we have to decrease the attempt by one
                elif mode == 2:
                    user_performance = (
                        db.query(models.TheoryEvalUserPerformance)
                        .filter(
                            and_(
                                models.TheoryEvalUserPerformance.email == email,
                                models.TheoryEvalUserPerformance.question_id
                                == question_id,
                            )
                        )
                        .order_by(models.TheoryEvalUserPerformance.timestamp.desc())
                        .first()
                    )
                    if user_performance and user_performance.user_attempts > 0:
                        db.delete(user_performance)

                db.commit()
                return True

        except OperationalError as e:
            retries += 1
            print(f"OperationalError encountered: {e}")
            time.sleep(retry_delay)

        except SQLAlchemyError as e:
            print("Error updating database:", e)
            db.rollback()
            return False

    if retries == max_retries:
        print("Maximum retries reached. Returning default response.")
        return False


# =========================================================================================
def delete_user_performance(
    email: pydantic.EmailStr,
    question_id: UUID,
    max_retries: int = 3,
    retry_delay: int = 2,
):
    retries = 0

    while retries < max_retries:
        try:
            with get_db() as db:
                query = db.query(models.TheoryEvalUserPerformance).filter(
                    models.TheoryEvalUserPerformance.email == email
                )
                if question_id != UUID("00000000-0000-0000-0000-000000000000"):
                    query = query.filter(
                        models.TheoryEvalUserPerformance.question_id == question_id
                    )

                user_performance = query.all()

                if user_performance:
                    for qn in user_performance:
                        db.delete(qn)
                    db.commit()
                    return True

        except OperationalError as e:
            print(f"OperationalError: {e}. Retrying...")
            retries += 1
            time.sleep(retry_delay)

        except SQLAlchemyError as e:
            print("Error querying database:", e)
            return False

    return False


# def update_user_performance(
#     email, question, llm_evaluation, llm_score, max_retries=3, retry_delay=2
# ):
#     """
#     Update the user performance with llm evaluation and scoring at the latest TIMESTAMP.

#     Parameters:
#     - edx_user_id (int): The edx user ID for which to update the database.
#     - llm_evaluation (str): The llm's evaluation based on the user's response.
#     - llm_score (int): The score given by llm based on the user's response.
#     - max_retries (int): Maximum number of retries for the operation.
#     - retry_delay (int): Delay between retries in seconds.

#     Returns:
#     - None
#     """
#     retries = 0
#     while retries < max_retries:
#         try:
#             with get_db() as db:
#                 # Retrieve the user performance record from the database
#                 user_performance = (
#                     db.query(models.TheoryEvalUserPerformance)
#                     .filter(
#                         and_(
#                             models.TheoryEvalUserPerformance.email == email,
#                             models.TheoryEvalUserPerformance.question == question,
#                         )
#                     )
#                     .order_by(desc(models.TheoryEvalUserPerformance.TIMESTAMP))
#                     .first()
#                 )

#                 # If the user performance record exists, update the user_attempts field and insert a new row
#                 if user_performance:
#                     user_performance.llm_evaluation = llm_evaluation
#                     user_performance.llm_score = llm_score
#                     db.commit()
#                 return

#         except OperationalError as e:
#             print(f"OperationalError: {e}. Retrying...")
#             retries += 1
#             time.sleep(retry_delay)

#         except SQLAlchemyError as e:
#             print("Error updating database:", e)
#             db.rollback()
#             break

#     if retries == max_retries:
#         print("Maximum retries reached. Update operation failed.")


# def create_user_attempt(
#     edx_user_id, email, question, user_response, max_retries=3, retry_delay=2
# ):
#     """
#     Increment the user_attempts value for a given user_id, apppend the question and the user's response and insert a new row into the database.

#     Parameters:
#     - edx_user_id (int): The edx user ID for which to update the database.
#     - question (str): The question user has attempted.
#     - user_response(str): The user's answer to the question.
#     - max_retries (int): Maximum number of retries for the operation due to OperationalError.
#     - retry_delay (int): Delay between retries in seconds.

#     Returns:
#     - None
#     """
#     retries = 0
#     while retries < max_retries:
#         try:
#             with get_db() as db:
#                 user_performance = (
#                     db.query(models.TheoryEvalUserPerformance)
#                     .filter(
#                         and_(
#                             models.TheoryEvalUserPerformance.email == email,
#                             models.TheoryEvalUserPerformance.question == question,
#                         )
#                     )
#                     .order_by(models.TheoryEvalUserPerformance.TIMESTAMP.desc())
#                     .first()
#                 )

#                 # If the user performance record exists, update the user_attempts field and insert a new row
#                 if user_performance:
#                     if user_performance.user_attempts == 3:
#                         print("User has reached the maximum attempt limit.")
#                         return
#                     else:
#                         user_performance.user_attempts += 1
#                         db.add(
#                             models.TheoryEvalUserPerformance(
#                                 edx_user_id=edx_user_id,
#                                 email=email,
#                                 question=question,
#                                 user_response=user_response,
#                                 user_attempts=user_performance.user_attempts,
#                             )
#                         )
#                 # If the user performance record doesn't exist, insert a new row
#                 else:
#                     # print("User performance record not found, inserting a new row.")
#                     db.add(
#                         models.TheoryEvalUserPerformance(
#                             edx_user_id=edx_user_id,
#                             email=email,
#                             question=question,
#                             user_response=user_response,
#                             user_attempts=1,
#                         )
#                     )

#                 db.commit()

#         except OperationalError as e:
#             print(f"OperationalError: {e}. Retrying...")
#             retries += 1
#             time.sleep(retry_delay)
#             db.rollback()

#         except SQLAlchemyError as e:
#             print("Error updating database:", e)
#             db.rollback()
#             return  # Exit on non-retryable error

#     if retries == max_retries:
#         print("Maximum retries reached. Operation failed.")
