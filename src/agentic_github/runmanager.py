import asyncio
import os
from agents import ItemHelpers, RunConfig, Runner
from agentic_github.coding_assistant import coding_agent
from agents.mcp import MCPServerStreamableHttp

GITHUB_PAT_KEY = os.getenv("GITHUB_PAT")

async def run_coding_agent_with_logs(prompt: str):
    """
    Run the coding agent and stream logs about what's happening
    """
    print("=== Run starting ===")
    print(f"[user] {prompt}\n")

    async with MCPServerStreamableHttp(
        name="Streamable Github MCP Server",        
        params={"url": "https://api.githubcopilot.com/mcp/", 
                "headers": {
                    "Authorization": f"Bearer {GITHUB_PAT_KEY}",
                },
                },
    ) as server:

        coding_agent.mcp_servers = [server]
        result = Runner.run_streamed(
            coding_agent,
            input=prompt
        )

        async for event in result.stream_events():
            
            # High-level items: messages, tool calls, tool outputs, MCP, etc.
            if event.type == "run_item_stream_event":
                item = event.item

                # 1) Tool calls (function tools, web_search, shell, MCP, etc.)
                if item.type == "tool_call_item":
                    raw = item.raw_item
                    raw_type_name = type(raw).__name__

                    # Special-case the ones we care most about in this cookbook
                    if raw_type_name == "ResponseFunctionWebSearch":
                        print("[tool] web_search_call – agent is calling web search")
                    elif raw_type_name == "LocalShellCall":
                        # LocalShellCall.action.commands is where the commands live
                        commands = getattr(getattr(raw, "action", None), "commands", None)
                        if commands:
                            print(f"[tool] shell – running commands: {commands}")
                        else:
                            print("[tool] shell – running command")
                    else:
                        # Generic fallback for other tools (MCP, function tools, etc.)
                        print(f"[tool] {raw_type_name} called")

                # 2) Tool call outputs
                elif item.type == "tool_call_output_item":
                    # item.output is whatever your tool returned (could be structured)
                    output_preview = str(item.output)
                    if len(output_preview) > 400:
                        output_preview = output_preview[:400] + "…"
                    print(f"[tool output] {output_preview}")

                # 3) Normal assistant messages
                elif item.type == "message_output_item":
                    text = ItemHelpers.text_message_output(item)
                    print(f"[assistant]\n{text}\n")

                # 4) Other event types (reasoning, MCP list tools, etc.) – ignore
                else:
                    pass

        print("=== Run complete ===\n")

        # Once streaming is done, result.final_output contains the final answer
        print("Final answer:\n")
        print(result.final_output)
