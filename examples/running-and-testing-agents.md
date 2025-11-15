# Running and Testing AI Agents - Complete Example

This guide demonstrates how to run and test the agents in this repository using OpenAI's API or other AI platforms.

## Prerequisites

- Python 3.8+ or Node.js 16+
- API key for your AI service (OpenAI, Azure OpenAI, Claude, etc.)
- A text editor or IDE

## Method 1: Using Python with OpenAI API

### Setup

1. **Install dependencies**:
```bash
pip install openai
```

2. **Set up your API key**:
```bash
# On Windows (PowerShell)
$env:OPENAI_API_KEY="your-api-key-here"

# On Windows (Command Prompt)
set OPENAI_API_KEY=your-api-key-here

# On macOS/Linux
export OPENAI_API_KEY="your-api-key-here"
```

### Running an Agent - Code Review Assistant Example

1. **Create a test script** (`test_code_review_agent.py`):

```python
import openai
import json
from pathlib import Path

# Configure API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load agent prompts
def load_prompt(file_path):
    """Load a prompt from a markdown file"""
    with open(file_path, 'r') as f:
        return f.read()

def run_agent(system_prompt, user_prompt, model="gpt-4", temperature=0.7):
    """Run an agent with given prompts"""
    response = openai.ChatCompletion.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content

# Load the Code Review Agent
system_prompt = load_prompt("agents/code-review-assistant/system-prompt.md")
user_prompt = load_prompt("agents/code-review-assistant/user-prompt-quick-review.md")

# Sample code to review
sample_code = """
def calculate_total(items):
    total = 0
    for item in items:
        total = total + item['price'] * item['quantity']
    return total

user_data = {'name': 'John', 'email': 'john@example.com'}
print(user_data)
"""

# Customize the user prompt with sample code
user_prompt = user_prompt.replace("[INSERT_CODE_HERE]", sample_code)

# Run the agent
print("🤖 Running Code Review Assistant...")
result = run_agent(system_prompt, user_prompt)
print("\n📝 Review Result:\n")
print(result)
```

2. **Run the script**:
```bash
python test_code_review_agent.py
```

### Expected Output

```
🤖 Running Code Review Assistant...

📝 Review Result:

## Code Review: Quick Review

### Critical Issues Found: 1

**Issue 1: Missing Error Handling**
- **Location**: `calculate_total()` function
- **Severity**: High
- **Description**: No validation for missing 'price' or 'quantity' keys
- **Fix**: Add key existence checks or use .get() with defaults
- **Code Example**:
  ```python
  price = item.get('price', 0)
  quantity = item.get('quantity', 0)
  ```

### Code Quality Notes
- Function is straightforward but lacks documentation
- Consider adding a docstring explaining parameters and return value
- Variable naming is clear and descriptive

### Recommended Next Steps
1. Add input validation
2. Add docstring documentation
3. Consider using sum() with a generator expression for clarity
```

## Method 2: Using cURL (No Installation Required)

### Running an Agent with cURL

```bash
# Set your API key
$env:OPENAI_API_KEY="your-api-key-here"

# Create a request
curl -X POST https://api.openai.com/v1/chat/completions `
  -H "Authorization: Bearer $env:OPENAI_API_KEY" `
  -H "Content-Type: application/json" `
  -d '{
    "model": "gpt-4",
    "temperature": 0.7,
    "messages": [
      {
        "role": "system",
        "content": "You are an expert code reviewer..."
      },
      {
        "role": "user",
        "content": "Please review this code: [code here]"
      }
    ]
  }'
```

## Method 3: Using Node.js/JavaScript

### Setup

1. **Install dependencies**:
```bash
npm install openai
```

2. **Create a test script** (`test_agent.js`):

```javascript
const fs = require('fs');
const OpenAI = require('openai');

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

async function loadPrompt(filePath) {
  return fs.readFileSync(filePath, 'utf-8');
}

async function runAgent(systemPrompt, userPrompt) {
  const completion = await client.chat.completions.create({
    model: "gpt-4",
    temperature: 0.7,
    messages: [
      { role: "system", content: systemPrompt },
      { role: "user", content: userPrompt }
    ]
  });
  
  return completion.choices[0].message.content;
}

async function main() {
  // Load prompts
  const systemPrompt = await loadPrompt(
    'agents/code-review-assistant/system-prompt.md'
  );
  const userPrompt = await loadPrompt(
    'agents/code-review-assistant/user-prompt-quick-review.md'
  );

  // Run agent
  console.log('🤖 Running Code Review Assistant...\n');
  const result = await runAgent(systemPrompt, userPrompt);
  console.log('📝 Result:\n', result);
}

main().catch(console.error);
```

3. **Run the script**:
```bash
node test_agent.js
```

## Testing Different Agents

### Testing the Technical Writer Agent

```python
# Load Technical Writer Agent
system_prompt = load_prompt("agents/technical-writer/system-prompt.md")
user_prompt = load_prompt("agents/technical-writer/user-prompt-api-docs.md")

# Customize with your API details
api_details = """
API Name: User Management API
Endpoints: 
- GET /users - List all users
- POST /users - Create new user
- GET /users/{id} - Get user by ID
- PUT /users/{id} - Update user
- DELETE /users/{id} - Delete user
"""

user_prompt = user_prompt.replace("[INSERT_API_DETAILS_HERE]", api_details)

# Run the agent
result = run_agent(system_prompt, user_prompt)
print(result)
```

## Testing Different User Prompts for Same Agent

### Code Review Agent - All Variants

```python
import json

def test_all_code_review_variants(code_to_review):
    """Test all variants of the code review agent"""
    system_prompt = load_prompt("agents/code-review-assistant/system-prompt.md")
    
    variants = [
        ("Quick Review", "agents/code-review-assistant/user-prompt-quick-review.md"),
        ("Comprehensive", "agents/code-review-assistant/user-prompt-comprehensive-review.md"),
        ("Security Focus", "agents/code-review-assistant/user-prompt-security-review.md")
    ]
    
    results = {}
    
    for variant_name, variant_file in variants:
        print(f"\n🔍 Testing: {variant_name}")
        print("=" * 50)
        
        user_prompt = load_prompt(variant_file)
        user_prompt = user_prompt.replace("[INSERT_CODE_HERE]", code_to_review)
        
        result = run_agent(system_prompt, user_prompt)
        results[variant_name] = result
        print(result)
    
    return results

# Example usage
sample_code = """
def validate_email(email):
    if '@' in email:
        return True
    return False
"""

test_all_code_review_variants(sample_code)
```

## Best Practices for Testing

### 1. **Test Data Preparation**

Create multiple test cases to validate agent behavior:

```python
test_cases = {
    "simple_function": """
        def add(a, b):
            return a + b
    """,
    "complex_authentication": """
        def login(username, password):
            user = db.query(username)
            if user.password == password:
                return generate_token(user)
    """,
    "performance_critical": """
        def process_large_dataset(data):
            results = []
            for item in data:
                results.append(process_item(item))
            return results
    """
}

for test_name, code in test_cases.items():
    print(f"\n📊 Testing: {test_name}")
    user_prompt = user_prompt_template.replace("[INSERT_CODE_HERE]", code)
    result = run_agent(system_prompt, user_prompt)
    print(result)
```

### 2. **Validate Output Quality**

```python
def validate_review_output(review_text):
    """Check if review has expected structure"""
    checks = {
        "has_critical_issues": "Critical Issues" in review_text,
        "has_recommendations": "Recommendation" in review_text,
        "has_code_examples": "```" in review_text,
        "substantive_length": len(review_text) > 200
    }
    return checks

result = run_agent(system_prompt, user_prompt)
validation = validate_review_output(result)
print(f"✅ Validation Results: {validation}")
```

### 3. **Monitor API Usage**

```python
def run_agent_with_tracking(system_prompt, user_prompt):
    """Run agent and track API usage"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0.7,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    
    # Track usage
    usage_info = {
        "input_tokens": response.usage.prompt_tokens,
        "output_tokens": response.usage.completion_tokens,
        "total_tokens": response.usage.total_tokens,
        "cost_estimate": response.usage.total_tokens * 0.00003  # GPT-4 pricing example
    }
    
    print(f"📊 Usage: {usage_info['total_tokens']} tokens (${usage_info['cost_estimate']:.4f})")
    
    return response.choices[0].message.content, usage_info
```

## Troubleshooting

### API Key Issues
```
Error: "Invalid API key provided"
Solution: Verify your API key in environment variables
- Check: echo $env:OPENAI_API_KEY
- Reset: $env:OPENAI_API_KEY="correct-key"
```

### File Not Found
```
Error: "FileNotFoundError: agents/code-review-assistant/system-prompt.md"
Solution: Run script from repository root directory
- Current: Run from c:\src\nipaul\ai-agents-prompts\
```

### Rate Limiting
```
Error: "Rate limit exceeded"
Solution: Add retry logic with exponential backoff
import time
for attempt in range(3):
    try:
        result = run_agent(system_prompt, user_prompt)
        break
    except RateLimitError:
        wait_time = 2 ** attempt
        time.sleep(wait_time)
```

## Next Steps

1. **Customize agents** for your specific use cases
2. **Create new agents** using the templates in `templates/`
3. **Batch test** multiple agents and compare results
4. **Integrate** into your development workflow
5. **Track improvements** as you refine prompts

For more details, see:
- [README.md](../README.md) - Overview and structure
- [USAGE_GUIDE.md](USAGE_GUIDE.md) - Detailed usage instructions
- [Agent Examples](.) - Other example implementations
