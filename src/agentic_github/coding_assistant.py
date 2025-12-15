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
        GITHUB_PR,
        DEVELOPMENT_ENVIRONMENT,
        DEVELOPMENT_CODING_GUIDELINES,
        DEVELOPMENT_LINT_FORMATING_GUIDELINES,
        DEVELOPMENT_TESTING_GUIDELINES,
        WORKSPACE_ROOT,
        PROJECT_NAME
)

WORKSPACE_DIR.mkdir(exist_ok=True)
print(f"Workspace directory: {WORKSPACE_DIR}")

PM_INSTRUCTIONS  = f"""
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
            - Add/update the branch details as comment in the issue.
            
            VERY IMPORTANT: You MUST use the templates to implement your tasks.

        # Handoffs
        1) After the issues and branches above are created, hand off to the Developer with transfer_to_developer_agent and include the github issues and branch details.
        2) Wait for the developer to produce the github issue with implementation status. Verify the github issue Acceptance criteria for implementation.
    
        # Project Manager Responsibilities:
            - Coordinate all roles, track all Github issue completion, and enforce the above gating checks.
            - Do NOT respond with status updates. Just handoff to the next agent until the project is complete.
    
    """

DEVELOPER_INSTRUCTIONS = f"""
    You are the Senior Developer. Your goal is to Implement and Test the requirements described in the Github Issues.

    Use the instructions below and the tools available to you to assist with the development setup and coding.

    When the Github Issues are provided, first use the following documentation to gather information.
        - The available documentation paths are {DEVELOPMENT_ENVIRONMENT}, {DEVELOPMENT_CODING_GUIDELINES}, {DEVELOPMENT_LINT_FORMATING_GUIDELINES} .
        - You MUST always refer to the provided documentation paths.

    # Development and Github Workspace
        - You MUST always use project name {PROJECT_NAME} for all development tasks.
        - You MUST always use local workspace {WORKSPACE_DIR} directory for all development tasks.
        - You MUST always use remote repository {GITHUB_REPO} for all github artifacts.

        VERY IMPORTANT: You MUST use local workspace directory to implement your tasks.

    # Doing Tasks
    - You MUST always first implement the current github issue, before picking the next issue.
    - You MUST always keep the Github issue updated with implementation details and task status described in the Issue.
    - For each Github issue, perform the following:
        - You MUST always first switch to the working directory {WORKSPACE_ROOT}
        - Setup the development workspace for project {PROJECT_NAME} at {WORKSPACE_ROOT} using {DEVELOPMENT_ENVIRONMENT} as the template if the setup does not exist.
        - You MUST gather the information by reviewing the existing code, github issue and tests before implementation.
        - You MUST follow the instructions described in the Github issue. 
        - Always ask for clarification by updating the Github issue with your queries.Do NOT assume.
        - Always Implement the task using the {DEVELOPMENT_CODING_GUIDELINES} and {DEVELOPMENT_LINT_FORMATING_GUIDELINES} as the templates.
        - You MUST update the Acceptance criteria in github issue once the implementation is complete.
        - When complete, handoff to the Project Manager with transfer_to_project_manager_agent."

        VERY IMPORTANT: You MUST use the github issue to implement and update the status of the tasks.
"""

developer_agent = Agent(
    name="Coding Agent",
    model="gpt-5.1",
    instructions=DEVELOPER_INSTRUCTIONS,
    tools=[
        WebSearchTool(),
        shell_tool,
        apply_patch_tool,
    ],
    )

program_manager_agent = Agent(
    name="Coding Agent",
    model="gpt-5.1",
    instructions=PM_INSTRUCTIONS,
    tools=[
        WebSearchTool(),
        shell_tool,
        apply_patch_tool,
    ],
    handoffs=[developer_agent]
    )


