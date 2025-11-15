# Quick Reference: Running Agents

## TL;DR - Get Started in 60 Seconds

### 1. Install OpenAI Package
```bash
pip install openai
```

### 2. Set Your API Key
```powershell
# Windows PowerShell
$env:OPENAI_API_KEY="sk-..."
```

### 3. Run the Agent
```bash
python examples/test_agent.py
```

**That's it!** You'll see a code review of the example code.

---

## Common Commands

### List Available Agents
```bash
python examples/test_agent.py --list
```

### Show Agent Details
```bash
python examples/test_agent.py --info code-review-assistant
```

### Run Different Variants
```bash
# Quick review (default)
python examples/test_agent.py

# Comprehensive review
python examples/test_agent.py --variant comprehensive-review

# Security-focused review
python examples/test_agent.py --variant security-review
```

### Review Your Own Code
```bash
python examples/test_agent.py --code "def hello(): return True"
```

### Use Different Model
```bash
python examples/test_agent.py --model gpt-4
```

### Technical Writer Examples
```bash
# API documentation
python examples/test_agent.py --agent technical-writer --variant api-docs

# Getting started guide
python examples/test_agent.py --agent technical-writer --variant getting-started

# Troubleshooting guide
python examples/test_agent.py --agent technical-writer --variant troubleshooting
```

---

## Manual Setup (No Script)

If you prefer to run agents manually in Python:

```python
import openai
openai.api_key = "your-key-here"

# Load prompts
system_prompt = open("agents/code-review-assistant/system-prompt.md").read()
user_prompt = open("agents/code-review-assistant/user-prompt-quick-review.md").read()

# Your code to review
code = """
def calculate_total(items):
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total
"""

user_prompt = user_prompt.replace("[INSERT_CODE_HERE]", code)

# Run agent
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

print(response.choices[0].message.content)
```

---

## Troubleshooting

### "OPENAI_API_KEY not found"
```powershell
# Set it
$env:OPENAI_API_KEY="sk-..."

# Verify
echo $env:OPENAI_API_KEY
```

### "ModuleNotFoundError: No module named 'openai'"
```bash
pip install openai
```

### "Invalid API key"
- Check your key at https://platform.openai.com/api-keys
- Make sure it's current (not expired)
- Try re-setting the environment variable

### "Rate limit exceeded"
- Wait a minute and try again
- Upgrade to a paid API plan if needed

### "Agent not found"
```bash
# List available agents
python examples/test_agent.py --list
```

---

## Next Steps

1. **Review the full guide**: [Running and Testing AI Agents](./running-and-testing-agents.md)
2. **Customize agents** for your use cases
3. **Create new agents** using templates in `templates/`
4. **Integrate** into your workflow

For detailed documentation, see [USAGE_GUIDE.md](../docs/USAGE_GUIDE.md)
