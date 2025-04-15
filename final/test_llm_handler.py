
from unittest.mock import patch

def test_openai_llm_initialization():
    with patch('theory_evaluation.llm_handler.AzureOpenAI') as mock_azure, \
         patch('theory_evaluation.llm_handler.OpenAI') as mock_openai, \
         patch('theory_evaluation.llm_handler.os.getenv', return_value='mock_value'):
        pass

from unittest.mock import patch, MagicMock

def test_openai_json_completion():
    with patch('theory_evaluation.llm_handler.OpenAI_llm.client', create=True) as mock_client:
        mock_response = MagicMock()
        mock_response.choices[0].message.content = '{"answer": "42", "explanation": "The answer to life."}'
        mock_client.chat.completions.create.return_value = mock_response

from unittest.mock import patch, MagicMock
from theory_evaluation.llm_handler import OpenAI_llm

def test_openai_streaming():
    with patch.object(OpenAI_llm, 'client', create=True) as mock_client:
        mock_stream = MagicMock()
        mock_chunk = MagicMock()
        mock_chunk.choices[0].delta.content = "streamed content"
        mock_stream.__iter__.return_value = [mock_chunk]
        mock_client.chat.completions.create.return_value = mock_stream

from unittest.mock import patch

def test_execute_text_generation():
    with patch('theory_evaluation.llm_handler.OpenAI_llm._run') as mock_run:
        mock_run.return_value.__aiter__.return_value = ["response content"]

from unittest.mock import patch

def test_execute_vision():
    with patch('theory_evaluation.llm_handler.OpenAI_llm._run') as mock_run:
        mock_run.return_value.__aiter__.return_value = ["response content"]
