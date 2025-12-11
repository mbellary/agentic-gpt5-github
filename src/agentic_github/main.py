import asyncio
from pathlib import Path

from agentic_github.runmanager import run_coding_agent_with_logs

workspace_dir = Path("C:/Users/bmoha/Work/agentic/agentic-workspace/greetings-lib").resolve()
workspace_dir.mkdir(exist_ok=True)

print(f"Workspace directory: {workspace_dir}")

github_issues_doc = ""
github_branch_doc = ""

TASK_LIST_PREFIX = "add a new greet function in greetings.py that takes name of the user and place of the user as inputs and prints a message 'Hello {name} from {place}' "

tpm_instructions = f"""
    Task List:
    - {TASK_LIST_PREFIX}

    You are the Technical Project Manager.

    Objective:
    Convert the input task lists into Github artifacts the team will execute against:

    Github Deliverables:
    - For each of the input tasks, please perform the following:
        - Add one github issue.
    - please refer to Agents.md located in the root directory of this repository for the details.
"""


#prompt = "please summarize the repository"
#prompt = "please list the contents of the pyproject.toml file from the repository"

async def run_agent():
    await run_coding_agent_with_logs(tpm_instructions)

def run():
    asyncio.run(run_agent())