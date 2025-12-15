import os
from dotenv import load_dotenv, dotenv_values
from pathlib import Path


PACKAGE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(PACKAGE_DIR / ".env")

def _env(name, default=None):
    v = os.getenv(name)
    return v if v is not None else default


GITHUB_PAT_KEY = _env("GITHUB_PAT_KEY", "")
GITHUB_REPO = _env("GITHUB_REPO", "")

WORKSPACE_ROOT = Path(_env("WORKSPACE_ROOT", "C:/Users/bmoha/Work/agentic/agentic-workspace/"))
PROJECT_NAME = _env("PROJECT_NAME", "greetings-lib")

WORKSPACE_DIR = Path(_env("WORKSPACE_DIR", "")).resolve()

OPENAI_API_KEY = _env("OPENAI_API_KEY", "")

GITHUB_COLAB = WORKSPACE_DIR / Path(_env("GITHUB_COLAB", ""))
GITHUB_BRANCH= WORKSPACE_DIR / Path(_env("GITHUB_BRANCH", ""))
GITHUB_BUG= WORKSPACE_DIR / Path(_env("GITHUB_BUG", ""))
GITHUB_FEATURE= WORKSPACE_DIR / Path(_env("GITHUB_FEATURE", ""))
GITHUB_PR= WORKSPACE_DIR / Path(_env("GITHUB_PR", ""))

DEVELOPMENT_ENVIRONMENT = WORKSPACE_DIR / Path(_env("DEVELOPMENT_ENVIRONMENT", ""))
DEVELOPMENT_CODING_GUIDELINES= WORKSPACE_DIR / Path(_env("DEVELOPMENT_CODING_GUIDELINES", ""))
DEVELOPMENT_LINT_FORMATING_GUIDELINES= WORKSPACE_DIR / Path(_env("DEVELOPMENT_LINT_FORMATING_GUIDELINES", ""))
DEVELOPMENT_TESTING_GUIDELINES= WORKSPACE_DIR / Path(_env("DEVELOPMENT_TESTING_GUIDELINES", ""))
