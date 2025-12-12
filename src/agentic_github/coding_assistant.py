import os
import asyncio
from agents import Agent, Runner, WebSearchTool, trace
from agentic_github.shellmanager import shell_tool
from agents.mcp import MCPServer, MCPServerStreamableHttp

GITHUB_PAT_KEY = os.getenv("GITHUB_PAT")

# Define the agent's instructions
INSTRUCTIONS = '''
You are a coding assistant. The user will explain what they want to build, and your goal is to run commands to generate a new app.
You can search the web to find which command you should use based on the technical stack, and use commands to create code files. 
You should use github server for creating issues.
You should also install necessary dependencies for the project to work. 
'''
directory_path = 'C:\\Users\\bmoha\\Work\\agentic\\agentic-workspace\\greetings-lib'
GITHUB_INSTRUCTIONS = f"Answer questions about the git repository at {directory_path}, use that for repo_path",



coding_agent = Agent(
    name="Coding Agent",
    model="gpt-5.1",
    instructions=INSTRUCTIONS,
    tools=[
        WebSearchTool(),
        shell_tool
    ],
    )
