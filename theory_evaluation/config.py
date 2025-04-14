# import pydantic

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Configuration class for application settings

    Attributes:
        API_NAME (str): The name of the API. Default is "project_simulation_fastapi".
        API_V1_STR (str): The base URL path for version 1 of the API. Default is "/api/v1".
        LOGGER_CONFIG_PATH (str): The file path to the logging configuration file. Default is "../conf/base/logging.yml".
    """

    API_NAME: str = "project_simulation_fastapi"
    API_V1_STR: str = "/api/v1"
    LOGGER_CONFIG_PATH: str = "../conf/base/logging.yml"


SETTINGS = Settings()
