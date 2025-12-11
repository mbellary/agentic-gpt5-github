import os
from agents import Agent, Runner, WebSearchTool
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

async def run(github_server: MCPServer):
    coding_agent = Agent(
        name="Coding Agent",
        model="gpt-5.1",
        instructions=INSTRUCTIONS,
        tools=[
            WebSearchTool(),
            shell_tool
        ],
        mcp_servers=[github_server]
    )
    return coding_agent

async def assistant():
    # Ask the user for the directory path
    #directory_path = input("Please enter the path to the git repository: ")

    async with MCPServerStreamableHttp(
        name="Streamable Github MCP Server",        
        params={"url": "https://api.githubcopilot.com/mcp/", 
                "headers": {
                    "Authorization": f"Bearer {GITHUB_PAT_KEY}",
                },
                },
    ) as server:
            await run(server)


coding_agent = Agent(
    name="Coding Agent",
    model="gpt-5.1",
    instructions=INSTRUCTIONS,
    tools=[
        WebSearchTool(),
        shell_tool
    ],
        #mcp_servers=[github_server]
    )