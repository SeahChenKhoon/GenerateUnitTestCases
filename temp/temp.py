
import asyncio
import json
import os
import pytest
from unittest.mock import patch
from openai import AzureOpenAI, OpenAI
from theory_evaluation.llm_handler import OpenAI_llm


# New Test Case
import pytest_asyncio
