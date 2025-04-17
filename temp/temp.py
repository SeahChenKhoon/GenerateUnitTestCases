from theory_evaluation import config
from theory_evaluation.evaluator import general_qa
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import logging
from theory_evaluation.main import health_check, shutdown_event, startup_event
import pytest