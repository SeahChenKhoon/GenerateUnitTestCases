## 🔧 2. Setup Virtual Environment & Install Dependencies

```
pip install uv
uv init
C:/Users/User/AppData/Local/Programs/Python/Python313/python.exe -m venv .venv
source .\\.venv\\Scripts\\activate
uv pip install -r requirements.txt
uv run ./src/rag_document_retrieval.py
pre-commit install
```

uv run generate_tests.py
PYTHONPATH=. uv run pytest -v tests/test_ConvertFtToMeters.py

 pre-commit run generate-tests --all-files --verbose

pytest tests/test_math_utils.py -v

Uninstall pre-commit
- uv pip uninstall pre-commit

pre-commit install
pip install pre-commit
pre-commit install