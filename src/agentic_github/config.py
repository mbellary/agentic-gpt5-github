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

WORKSPACE_DIR = Path(_env("WORKSPACE_DIR", "")).resolve()

OPENAI_API_KEY = _env("OPENAI_API_KEY", "")

GITHUB_COLAB = WORKSPACE_DIR / Path(_env("GITHUB_COLAB", ""))
GITHUB_BRANCH= WORKSPACE_DIR / Path(_env("GITHUB_BRANCH", ""))
GITHUB_BUG= WORKSPACE_DIR / Path(_env("GITHUB_BUG", ""))
GITHUB_FEATURE= WORKSPACE_DIR / Path(_env("GITHUB_FEATURE", ""))
GITHUB_PR= WORKSPACE_DIR / Path(_env("GITHUB_PR", ""))