## 🔧 2. Setup Virtual Environment & Install Dependencies

```
pip install uv
uv init
C:/Users/User/AppData/Local/Programs/Python/Python313/python.exe -m venv .venv
source .\\.venv\\Scripts\\activate
uv pip install -r requirements.txt
uv run ./src/rag_document_retrieval.py
```

uv run generate_tests.py
PYTHONPATH=. uv run pytest -v tests/test_ConvertFtToMeters.py

