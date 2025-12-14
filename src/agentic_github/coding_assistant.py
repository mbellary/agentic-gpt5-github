import os
import asyncio
from pathlib import Path
from typing import List
from agents import Agent, Runner, WebSearchTool
from agentic_github.shellmanager import shell_tool
from agentic_github.apply_patch import apply_patch_tool
from agentic_github.config import (
        GITHUB_REPO, 
        WORKSPACE_DIR,
        GITHUB_COLAB,
        GITHUB_BRANCH,
        GITHUB_FEATURE,
        GITHUB_BUG,
        GITHUB_PR
)

WORKSPACE_DIR.mkdir(exist_ok=True)
print(f"Workspace directory: {WORKSPACE_DIR}")

# # Define the TodoWrite function as a tool
# @tool
# def todo_write(tasks: List[str]) -> str:
#     """
#     Write a todo list to help the agent organize its thoughts and track progress.

#     Args:
#         tasks: A list of task descriptions.
#     """
#     # This function is for organizational purposes only and doesn't perform actions.
#     # It just returns a confirmation string.
#     return f"Todo list updated with {len(tasks)} tasks."

INSTRUCTIONS  = f"""
        You are the Program Manager. Your goal is to manage and track the Github artifacts the team will execute against.
        
        Use the instructions below and the tools available to you to assist the user.

        When the user provides the tasks, first use the following documentation to gather information.
            - The available documentation paths are {GITHUB_COLAB}, {GITHUB_BRANCH}, {GITHUB_BUG}, {GITHUB_FEATURE} and {GITHUB_PR} .
            - You MUST always refer to the provided documentation paths.
        
        
        # Github Artifacts
            - You MUST use remote repository {GITHUB_REPO} for all github artifacts.

            
            
        # Doing Tasks
        - for user provided tasks, you MUST create separate Github artifacts if the tasks are not related or requires sub-tasks.
        - for each of the user provided task, perform the following:
            - Always first search if the task exist before adding or updating the github artifacts.
            - Add github issue using {GITHUB_BUG} or {GITHUB_FEATURE} as the template only if the issue does not exist.
            - Create branch using {GITHUB_BRANCH} as the template only if the branch does not exist.
            
            VERY IMPORTANT: You MUST use the templates to implement your tasks.

"""

print(INSTRUCTIONS)

program_manager_agent = Agent(
    name="Coding Agent",
    model="gpt-5.1",
    instructions=INSTRUCTIONS,
    tools=[
        WebSearchTool(),
        shell_tool,
        apply_patch_tool,
    ],
    )
