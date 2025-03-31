# ✅ Auto Unit Test Generator with Pre-commit Integration

This project automates the generation of pytest-style unit tests for Python files using OpenAI's large language models (LLMs). It integrates with pre-commit to automatically generate or update tests whenever a file in the `src/` directory is changed.

---

# 🎯 Objectives

- Automatically generate unit tests for updated Python files.
- Use OpenAI's GPT model for intelligent and comprehensive test generation.
- Save tests to the `tests/` directory in a mirrored folder structure.
- Stage test files for commit automatically.
- Run all unit tests after generation using `pytest`.

---

# ⚙️ Key Features

## 🧠 LLM-Powered Test Generation
- Uses OpenAI's `gpt-4-turbo` or configurable model from `.env`.
- Prompts include extracted imports and function names for context.
- Ensures all public functions are tested with meaningful test names.

## 🧪 Pre-commit Hook Integration
- Automatically triggers test generation when files in `src/` change.
- Stages newly created test files using `git add`.
- Runs all tests via `pytest` after generation.
- Includes CLI logging to track processing and errors.

## 📁 Test File Management
- Tests saved in `tests/` directory with mirrored structure:
  e.g., `src/module.py` → `tests/test_module.py`.
- Ensures consistent naming conventions and UTF-8 encoding.

## 🌐 Environment Variables via `.env`
- Configure source and test directories.
- Model name and LLM prompt template are customizable.
- Example:
  ```env
  OPENAI_API_KEY=your_openai_key
  SRC_DIR=./src
  TESTS_DIR=./tests
  MODEL_NAME=gpt-4-turbo
  LLM_TEST_PROMPT_TEMPLATE=...