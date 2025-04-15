import json
import pytest
from unittest.mock import patch, MagicMock
from theory_evaluation.llm_handler import OpenAI_llm

@pytest.fixture
def mock_openai_llm():
    with patch("theory_evaluation.llm_handler.AzureOpenAI") as mock_azure_openai, \
         patch("theory_evaluation.llm_handler.OpenAI") as mock_openai, \
         patch("theory_evaluation.llm_handler.os.getenv", side_effect=lambda key: f"{key}_value"):
        yield mock_azure_openai, mock_openai

@pytest.mark.asyncio
async def test_openai_llm_initialization(mock_openai_llm):
    mock_azure_openai, mock_openai = mock_openai_llm
    llm = OpenAI_llm(
        useAzureOpenAI=True,
        message="Test message",
        output="json",
        mode="text_generation",
        verbose=True
    )
    
    assert llm.message == "Test message"
    assert llm.output == "json"
    assert llm.mode == "text_generation"
    assert llm.verbose is True
    assert hasattr(llm, "client")
    assert mock_azure_openai.called

@pytest.mark.asyncio
async def test_openai_json_completion():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = json.dumps({"answer": "42", "explanation": "The answer to everything."})
    
    with patch("theory_evaluation.llm_handler.OpenAI_llm.client") as mock_client:
        mock_client.chat.completions.create.return_value = mock_response
        
        llm = OpenAI_llm(message="Test message")
        content = await llm._OpenAI_JSON_Completion(messages=[{"role": "system", "content": llm.message}])
        
        assert content == {"answer": "42", "explanation": "The answer to everything."}

@pytest.mark.asyncio
async def test_openai_streaming():
    mock_chunk = MagicMock()
    mock_chunk.choices[0].delta.content = "streaming content"
    
    with patch("theory_evaluation.llm_handler.OpenAI_llm.client") as mock_client:
        mock_client.chat.completions.create.return_value = [mock_chunk]
        
        llm = OpenAI_llm(message="Test message", output="stream")
        async for data in llm._OpenAI_Streaming(messages=[{"role": "system", "content": llm.message}]):
            assert data == "streaming content"

@pytest.mark.asyncio
async def test_openai_chat_completion():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "chat completion content"
    
    with patch("theory_evaluation.llm_handler.OpenAI_llm.client") as mock_client:
        mock_client.chat.completions.create.return_value = mock_response
        
        llm = OpenAI_llm(message="Test message")
        content = await llm._OpenAI_Chat_Completion(messages=[{"role": "system", "content": llm.message}])
        
        assert content == "chat completion content"

@pytest.mark.asyncio
async def test_execute_text_generation():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "text generation response"
    
    with patch("theory_evaluation.llm_handler.OpenAI_llm.client") as mock_client:
        mock_client.chat.completions.create.return_value = mock_response
        
        llm = OpenAI_llm(message="Test message", output=None, mode="text_generation")
        async for response in llm.execute():
            assert response == "text generation response"

@pytest.mark.asyncio
async def test_execute_vision_mode():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "vision response"
    
    with patch("theory_evaluation.llm_handler.OpenAI_llm.client") as mock_client:
        mock_client.chat.completions.create.return_value = mock_response
        
        llm = OpenAI_llm(message="Test message", output=None, mode="vision", image_input="image_data")
        async for response in llm.execute():
            assert response == "vision response"
o
