import asyncio
from pathlib import Path

from agentic_github.runmanager import run_coding_agent_with_logs

github_respository = "https://github.com/mbellary/greetings-lib"
workspace_dir = Path("C:/Users/bmoha/Work/agentic/agentic-workspace/greetings-lib").resolve()
workspace_dir.mkdir(exist_ok=True)
print(f"Workspace directory: {workspace_dir}")

TASK_LIST_PREFIX = '''
    1) add a new greet function in greetings.py that takes name of the user and place of the user as inputs and prints a message 'Hello {name} from {place}' 
    2) add a new bye function in bye.py that takes name of the user and place of the user as inputs and prints a message 'Bye {name} !!'
    '''

tpm_instructions = f"""
    Task List:
        {TASK_LIST_PREFIX}

    You are the Technical Project Manager.

    Objective:
    Convert the input task lists into Github artifacts the team will execute against:

    Details:
    - local repository is located at {workspace_dir}
    - remote repository is located at {github_respository}
    - you must follow guidelines defined in Agents.md located in the root directory of the local repository for the details.

    Deliverables:
    - For each of the input tasks, please perform the following:
        - Add a github issue.
        - Add a corresponding branch. you must create a new branch from 'main' always.
        - you must link the issue to this branch by adding a comment with the branch name in issue.
"""


#prompt = "please summarize the repository"
#prompt = "please list the contents of the pyproject.toml file from the repository"

async def run_agent():
    await run_coding_agent_with_logs(tpm_instructions)

def run():
    asyncio.run(run_agent())