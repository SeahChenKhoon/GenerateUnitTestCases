## llm_handler.py
import asyncio
import json
import os

from openai import AzureOpenAI, OpenAI

DEFAULT_CONFIG = {
    "temperature": 0,
    "max_tokens": 1000,
    "top_p": 1.0,
    "frequency_penalty": 0.0,  # penalty for the model for generating high-frequency words.
    "presence_penalty": 0.0,  # negative value encourage the model to include specific words from the input prompt into the response output.
}
DEFAULT_MESSAGE = """
    You are a helpful assistant designed to answer and give tips on any queries.
"""


class OpenAI_llm:
    # Initialisation of LLM Class
    def __init__(
        self,
        useAzureOpenAI: bool = False,
        azure_endpoint: str | None = None,
        message: str = DEFAULT_MESSAGE,
        image_input: str | None = None,
        api_version: str | None = None,
        model_name: str | None = None,  # if None, model as stated in default config
        max_retries: int = 3,
        output: str | None = None,
        mode: str = "text_generation",
        config: dict = DEFAULT_CONFIG,
        verbose: bool = False,
    ) -> None:
        assert (
            message is not None and message.strip() != ""
        ), "Prompt message must be inserted."
        assert output in [
            "json",
            "stream",
            None,
        ], "Output must be either 'json', 'stream', or None"
        assert mode in [
            "text_generation",
            "vision",
        ], "mode must be either 'text_generation' or 'vision'"

        self.message = message
        self.image_input = image_input
        self.azure_endpoint = azure_endpoint or os.getenv(
            "AZURE_OPENAI_ENDPOINT_SWEDEN"
        )
        self.api_version = api_version or os.getenv("AZURE_OPENAI_API_VERSION")
        self.model_name = model_name
        self.max_retries = max_retries
        self.output = output
        self.mode = mode
        self.config = config
        self.verbose = verbose

        if useAzureOpenAI:
            self.client = AzureOpenAI(
                azure_endpoint=self.azure_endpoint,
                api_key=os.getenv("AZURE_OPENAI_API_KEY_SWEDEN"),
                api_version=self.api_version,
                max_retries=self.max_retries,
            )
        else:
            self.client = OpenAI(
                api_key=os.environ.get("OPENAI_API_KEY"),
            )

        if not self.model_name:  # model default based on env config, if None
            if useAzureOpenAI:
                self.model_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
            else:
                self.model_name = os.getenv("OPENAI_DEPLOYMENT_NAME")

    # Intrinsic functions
    async def _OpenAI_JSON_Completion(self, **kwargs):
        # Assuming the response is in the expected format and content is a JSON structure.
        try:
            response = self.client.chat.completions.create(
                **kwargs,
                response_format={"type": "json_object"},
                stream=False,
            )
            # Assuming content holds a JSON-like string that needs to be parsed.
            content = json.loads(response.choices[0].message.content)
            # print(json.dumps(content, indent=4))
            # print(content['answer'])
            # print(content['explanation'])
            return content
        except Exception as e:
            print("Failed in _OpenAI_JSON_Completion:", e)

    async def _OpenAI_Streaming(self, **kwargs):
        try:
            stream = self.client.chat.completions.create(
                **kwargs,
                stream=True,
            )
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    # print(chunk.choices[0].delta.content, end="")
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"Failed in _OpenAI_Streaming: {e}"

    async def _OpenAI_Chat_Completion(self, **kwargs):
        try:
            response = self.client.chat.completions.create(
                **kwargs,
                stream=False,
            )
            # print(response.choices[0].message.content, end="")
            return response.choices[0].message.content
        except Exception as e:
            print("Failed in _OpenAI_Chat_Completion:", e)

    async def _run(self, **kwargs):
        if self.output == "json":
            content = await self._OpenAI_JSON_Completion(**kwargs)
            yield content
        elif self.output == "stream":
            async for data in self._OpenAI_Streaming(**kwargs):
                yield data
        else:
            content = await self._OpenAI_Chat_Completion(**kwargs)
            yield content

    # Get LLM response ========
    async def execute(self):
        try:
            if self.mode == "text_generation":
                messages = [
                    {"role": "system", "content": self.message},
                ]
            elif self.mode == "vision":
                messages = [
                    {"role": "system", "content": self.message},
                    {
                        "role": "user",
                        "content": "Help me with the task regarding the image given.",
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{self.image_input}",
                                    "detail": "high",
                                },
                            }
                        ],
                    },
                ]

            if self.verbose:
                print(json.dumps(messages[0], indent=4))

            async for response in self._run(
                messages=messages, model=self.model_name, **self.config
            ):
                yield response
        except Exception as e:
            yield f"Error: {e}"


if __name__ == "__main__":
    # message = """
    # You are a AI teacher in math.
    # What is 2+5?
    # Return your response in the following json format:
    # ```
    # {
    #     "answer": [Your answer]
    #     "explanation": [Your explanation]
    # }
    # ```
    #     """

    message = """
    You are a helpful assistant.
    Does Azure OpenAI support customer managed keys?
    Do other Azure AI services support this too?
    """

    async def main():
        llm = OpenAI_llm(
            message=message, useAzureOpenAI=True, output="stream", verbose=True
        )

        async for token in llm.execute():  # Use async for to handle streaming
            print(token)

    asyncio.run(main())
