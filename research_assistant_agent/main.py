# |---------------------------------------------------------|
# |                                                         |
# |                 Give Feedback / Get Help                |
# | https://github.com/getbindu/Bindu/issues/new/choose    |
# |                                                         |
# |---------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""research-assistant-agent - A Simple Bindu Research Agent."""

import argparse
import asyncio
import json
import os
from pathlib import Path
from typing import Any

from bindu.penguin.bindufy import bindufy
from dotenv import load_dotenv

# Agno imports (simple agent)
from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Load environment variables
load_dotenv()

# Global agent instance
agent: Agent | None = None
model_name: str | None = None
openrouter_api_key: str | None = None
_initialized = False
_init_lock = asyncio.Lock()


def load_config() -> dict:
    """Load agent configuration."""
    config_path = Path(__file__).parent / "agent_config.json"
    with open(config_path, "r") as f:
        return json.load(f)


async def initialize_agent():
    """Initialize simple research agent."""
    global agent, _initialized

    if _initialized:
        return

    async with _init_lock:
        if _initialized:
            return

        agent = Agent(
            instructions=(
                "You are a helpful research assistant. "
                "Find information, explain clearly, and summarize concisely."
            ),
            model=OpenAIChat(
                id=model_name,
                api_key=openrouter_api_key,
                base_url="https://openrouter.ai/api/v1",
            ),
        )

        _initialized = True
        print("✅ Agent initialized")


# --- Async run_agent wrapper for tests ---
async def run_agent(messages: list[dict[str, str]]) -> Any:
    """Async wrapper for agent.run()."""
    if not agent:
        return None
    # simulate async behavior for testing
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, agent.run, {"input": messages})


async def handler(messages: list[dict[str, str]]) -> Any:
    """Handle incoming messages from Bindu."""
    await initialize_agent()
    return await run_agent(messages)


# --- For test compatibility ---
initialize_all = initialize_agent
initialize_mcp_tools = lambda: print("initialize_mcp_tools not implemented")


def main():
    """Run the Agent."""
    global model_name, openrouter_api_key

    parser = argparse.ArgumentParser(description="Simple Bindu Research Agent")
    parser.add_argument(
        "--model",
        type=str,
        default=os.getenv("MODEL_NAME", "openrouter/free"),
        help="Model ID to use from OpenRouter",
    )
    parser.add_argument(
        "--api-key",
        type=str,
        default=os.getenv("OPENROUTER_API_KEY"),
        help="OpenRouter API key",
    )

    args = parser.parse_args()

    model_name = args.model
    openrouter_api_key = args.api_key

    if not openrouter_api_key:
        raise ValueError("OPENROUTER_API_KEY required")

    print(f"🤖 Using model: {model_name}")

    config = load_config()

    print("🚀 Starting Bindu agent server...")
    bindufy(config, handler)


if __name__ == "__main__":
    main()