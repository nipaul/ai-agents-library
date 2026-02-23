#!/usr/bin/env python3
"""
Simple agent runner for testing AI agents in this repository.

Usage:
    python test_agent.py                    # Run default example
    python test_agent.py --agent code-review-assistant --variant quick-review
    python test_agent.py --agent technical-writer --variant api-docs

Requirements:
    - OpenAI API key in OPENAI_API_KEY environment variable
    - openai package: pip install openai
"""

import os
import sys
import json
import argparse
from pathlib import Path

try:
    import openai
    try:
        from openai import RateLimitError, AuthenticationError, APIConnectionError
    except Exception:
        RateLimitError = AuthenticationError = APIConnectionError = Exception
except ImportError:
    print("❌ Error: openai package not installed")
    print("Install it with: pip install openai")
    exit(1)


def load_prompt(file_path):
    """Load a prompt from a markdown or txt file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ Error: File not found: {file_path}")
        exit(1)


def load_env_file_if_missing(env_path=".env"):
    """Load key values from a .env file if OPENAI_API_KEY is missing."""
    if os.environ.get("OPENAI_API_KEY"):
        return
    if not Path(env_path).exists():
        return
    try:
        with open(env_path, 'r', encoding='utf-8') as f:
            for raw_line in f:
                line = raw_line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key and key not in os.environ:
                    os.environ[key] = value
    except Exception:
        # Best-effort only; environment can still be set manually.
        pass


def load_agent_config(agent_name):
    """Load agent configuration from config.json"""
    config_path = f"agents/{agent_name}/config.json"
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: Agent '{agent_name}' not found")
        print("Available agents:")
        if Path("agents").exists():
            for agent_dir in Path("agents").iterdir():
                if agent_dir.is_dir():
                    print(f"  - {agent_dir.name}")
        exit(1)


def get_user_prompt_file(agent_name, variant):
    """Get the user prompt file for a specific variant"""
    config = load_agent_config(agent_name)
    
    # Find the matching user prompt
    for prompt_config in config.get("user_prompts", []):
        if variant.lower() in prompt_config.get("name", "").lower():
            return f"agents/{agent_name}/{prompt_config['file']}"
    
    print(f"❌ Error: Variant '{variant}' not found for agent '{agent_name}'")
    print("Available variants:")
    for prompt_config in config.get("user_prompts", []):
        print(f"  - {prompt_config['name']}: {prompt_config.get('description', 'N/A')}")
    exit(1)


def run_agent(system_prompt, user_prompt, model="gpt-3.5-turbo", temperature=0.7):
    """Run an agent with given prompts using OpenAI API"""
    load_env_file_if_missing()
    if not openai.api_key:
        openai.api_key = os.environ.get("OPENAI_API_KEY")
    if not openai.api_key:
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Set it with:")
        print("  Windows (PowerShell): $env:OPENAI_API_KEY='your-key'")
        print("  Windows (CMD): set OPENAI_API_KEY=your-key")
        print("  macOS/Linux: export OPENAI_API_KEY='your-key'")
        exit(1)
    
    try:
        response = openai.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content
    except RateLimitError:
        print("❌ Error: Rate limit exceeded. Wait a moment and try again.")
        exit(1)
    except AuthenticationError:
        print("❌ Error: Invalid API key. Check your OPENAI_API_KEY.")
        exit(1)
    except APIConnectionError:
        print("❌ Error: Connection error. Check network access or proxy settings.")
        exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)


def print_agent_info(agent_name):
    """Print information about an agent"""
    config = load_agent_config(agent_name)
    agent_info = config.get("agent", {})
    
    print(f"\n📋 Agent: {agent_info.get('name', 'N/A')}")
    print(f"   Version: {agent_info.get('version', 'N/A')}")
    print(f"   Description: {agent_info.get('description', 'N/A')}")
    print(f"\n   Available variants:")
    for prompt in config.get("user_prompts", []):
        print(f"     • {prompt['name']}: {prompt.get('description', 'N/A')}")


def main():
    # Ensure UTF-8 output for emoji and non-ASCII text on Windows consoles.
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    parser = argparse.ArgumentParser(
        description="Run and test AI agents from this repository",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python test_agent.py                                          # Run default (quick code review)
  python test_agent.py --agent code-review-assistant --variant comprehensive-review
  python test_agent.py --agent technical-writer --variant api-docs
  python test_agent.py --list                                    # List available agents
        """
    )
    
    parser.add_argument(
        "--agent",
        default="code-review-assistant",
        help="Agent to run (default: code-review-assistant)"
    )
    parser.add_argument(
        "--variant",
        default="quick_review",
        help="User prompt variant to use (default: quick-review)"
    )
    parser.add_argument(
        "--model",
        default="gpt-3.5-turbo",
        help="OpenAI model to use (default: gpt-3.5-turbo)"
    )
    parser.add_argument(
        "--code",
        help="Code to review (if not provided, uses template from prompt)"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available agents and exit"
    )
    parser.add_argument(
        "--info",
        help="Show info about a specific agent"
    )
    
    args = parser.parse_args()
    
    # List agents
    if args.list:
        print("📚 Available Agents:\n")
        if Path("agents").exists():
            for agent_dir in sorted(Path("agents").iterdir()):
                if agent_dir.is_dir():
                    print_agent_info(agent_dir.name)
                    print()
        exit(0)
    
    # Show agent info
    if args.info:
        print_agent_info(args.info)
        exit(0)
    
    # Load prompts
    print(f"🤖 Loading {args.agent}...")
    system_prompt_path = f"agents/{args.agent}/system-prompt.md"
    user_prompt_path = get_user_prompt_file(args.agent, args.variant)
    
    system_prompt = load_prompt(system_prompt_path)
    user_prompt = load_prompt(user_prompt_path)
    
    # If code is provided via command line, replace in the user prompt
    if args.code:
        user_prompt = user_prompt.replace("[INSERT_CODE_HERE]", args.code)
    
    # Run the agent
    print(f"🚀 Running with variant: {args.variant}")
    print(f"📡 Using model: {args.model}")
    print("\n" + "="*60)
    print("AGENT OUTPUT:")
    print("="*60 + "\n")
    
    result = run_agent(system_prompt, user_prompt, model=args.model)
    print(result)
    
    print("\n" + "="*60)


if __name__ == "__main__":
    main()
