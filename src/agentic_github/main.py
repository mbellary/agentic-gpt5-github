import asyncio
from pathlib import Path

from agentic_github.runmanager import run_coding_agent_with_logs
from agentic_github.runeditmanager import run_updated_coding_agent_with_logs


TASK_LIST_PREFIX = '''
    1) add a new greet function in greetings.py that takes name of the user and place of the user as inputs and prints a message 'Hello {name} from {place}' 
    2) add a new bye function in bye.py that takes name of the user and return message 'Bye {name} !!'
    3) add a request that describes or defines the testing guidelines
    '''


#prompt = "please summarize the repository"
#prompt = "please list the contents of the pyproject.toml file from the repository"

async def run_agent():
    await run_updated_coding_agent_with_logs(TASK_LIST_PREFIX)

def run():
    asyncio.run(run_agent())