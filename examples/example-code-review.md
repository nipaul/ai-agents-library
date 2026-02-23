# Example: Code Review Assistant in Action

This document shows a complete example of running the Code Review Assistant agent and what the output looks like.

## Setup

```bash
# 1. Install OpenAI package
pip install openai

# 2. Set your API key
$env:OPENAI_API_KEY="sk-your-key-here"

# 3. Run the example
python examples/test_agent.py
```

## Sample Code Being Reviewed

```python
def calculate_total(items):
    total = 0
    for item in items:
        total = total + item['price'] * item['quantity']
    return total

def validate_email(email):
    if '@' in email:
        return True
    return False

def process_user_data(user_data):
    name = user_data['name']
    email = user_data['email']
    
    if validate_email(email):
        total = calculate_total(user_data['orders'])
        return {
            'name': name,
            'email': email,
            'total_spent': total
        }
    else:
        return None
```

## Running the Different Review Variants

### 1. Quick Review (Fast Feedback)

```bash
python examples/test_agent.py --variant quick_review
```

**Output Example:**
```
🤖 Loading code-review-assistant...
🚀 Running with variant: quick-review
📡 Using model: gpt-3.5-turbo

============================================================
AGENT OUTPUT:
============================================================

## Quick Code Review

### Critical Issues: 1

**Issue: Missing Error Handling**
- The `calculate_total()` function doesn't validate that items have 'price' and 'quantity' keys
- Could throw KeyError on malformed data
- **Fix**: Use `.get()` method or add validation

```python
def calculate_total(items):
    total = 0
    for item in items:
        price = item.get('price', 0)
        qty = item.get('quantity', 0)
        total += price * qty
    return total
```

### Recommendation
Add input validation before processing. Otherwise, code is functional for the happy path.
```

### 2. Comprehensive Review (Detailed Analysis)

```bash
python examples/test_agent.py --variant comprehensive-review
```

**Output Example:**
```
## Comprehensive Code Review

### Issues Found: 3

#### 1. Error Handling (High Priority)
- Missing validation in `calculate_total()`
- Missing try-catch in `process_user_data()`
- No null checks for dictionary access

#### 2. Code Quality (Medium Priority)
- No docstrings explaining function behavior
- Email validation is too simplistic (many edge cases)
- Magic strings ('price', 'quantity') should be constants

#### 3. Performance (Low Priority)
- Using `+=` in loop is fine for Python
- Consider using `sum()` with generator for clarity

### Recommendations
1. Add comprehensive input validation
2. Document all functions with docstrings
3. Create constants for magic strings
4. Improve email validation (use regex or library)
5. Add type hints
6. Create unit tests

### Refactored Example
```python
from typing import List, Dict, Optional
import re

# Constants
PRICE_KEY = 'price'
QUANTITY_KEY = 'quantity'
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def validate_email(email: str) -> bool:
    """Validate email format using regex."""
    return bool(re.match(EMAIL_REGEX, email))

def calculate_total(items: List[Dict]) -> float:
    """Calculate total from list of items with price and quantity."""
    try:
        return sum(
            item.get(PRICE_KEY, 0) * item.get(QUANTITY_KEY, 0)
            for item in items
        )
    except (TypeError, ValueError):
        raise ValueError("Invalid item format")

def process_user_data(user_data: Dict) -> Optional[Dict]:
    """Process user data and calculate total spent."""
    if not isinstance(user_data, dict):
        return None
    
    try:
        email = user_data.get('email')
        if not email or not validate_email(email):
            return None
        
        return {
            'name': user_data.get('name'),
            'email': email,
            'total_spent': calculate_total(user_data.get('orders', []))
        }
    except (KeyError, ValueError):
        return None
```
```

### 3. Security-Focused Review

```bash
python examples/test_agent.py --variant security-review
```

**Output Example:**
```
## Security-Focused Code Review

### Security Issues Found: 2

#### 1. Input Validation (HIGH SEVERITY)
**Vulnerability**: SQL Injection Risk (if database is used)
- User data comes unvalidated into functions
- Email validation is insufficient
- Recommendation: Validate all user inputs

#### 2. Data Exposure (MEDIUM SEVERITY)
**Vulnerability**: Potential Information Disclosure
- Processing user data without checking permissions
- No access control checks
- Recommendation: Add authorization checks

### Security Checklist
- [ ] Validate all inputs
- [ ] Sanitize email before using in SQL
- [ ] Add authentication/authorization
- [ ] Use type hints for defensive coding
- [ ] Add logging for security events
- [ ] Handle exceptions securely (no stack traces to users)
- [ ] Consider encryption for sensitive data

### Example Security Improvements
```python
import logging
from typing import Optional

logger = logging.getLogger(__name__)

def validate_and_sanitize_email(email: str) -> Optional[str]:
    """Validate and sanitize email input."""
    if not email or not isinstance(email, str):
        logger.warning("Invalid email input type")
        return None
    
    email = email.strip().lower()
    
    # Use email validation library
    try:
        from email_validator import validate_email, EmailNotValidError
        valid = validate_email(email)
        return valid.email
    except EmailNotValidError:
        logger.warning(f"Invalid email format: {email}")
        return None

def process_user_data_secure(user_data: Dict, user_id: int) -> Optional[Dict]:
    """Securely process user data with validation and authorization."""
    try:
        # Authorization check
        if not user_can_access(user_id, user_data):
            logger.warning(f"Unauthorized access attempt by user {user_id}")
            return None
        
        # Input validation
        email = validate_and_sanitize_email(user_data.get('email'))
        if not email:
            return None
        
        return {
            'name': sanitize_string(user_data.get('name')),
            'email': email,
            'total_spent': calculate_total_safe(user_data.get('orders', []))
        }
    except Exception as e:
        logger.error(f"Error processing user data: {type(e).__name__}")
        return None
```
```

## Comparing Variants

| Aspect | Quick Review | Comprehensive | Security Focus |
|--------|---|---|---|
| **Speed** | ⚡ Fast (perfect for dev) | 📊 Detailed (pre-merge) | 🔒 Security-first |
| **Issues Found** | Critical only | All levels | Security issues |
| **Recommendations** | Minimal | Extensive | Security hardening |
| **Examples** | Brief | Detailed | Security patterns |
| **Best For** | Daily development | Code review gates | Audits/compliance |
| **Output Length** | ~300 words | ~1000+ words | ~800 words |

## Running Multiple Reviews

```bash
# Test all variants
for variant in quick-review comprehensive-review security-review {
    Write-Host "=== $variant ==="
    python examples/test_agent.py --variant $variant
    Write-Host "`n`n"
}
```

## Integrating Into Workflow

### Pre-Commit Hook

Create `.git/hooks/pre-commit`:
```bash
#!/bin/bash
# Check code before committing

echo "Running Code Review Agent..."
python examples/test_agent.py --variant quick-review

# Ask user if they want to continue
read -p "Continue with commit? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    exit 1
fi
```

### CI/CD Pipeline

```yaml
# Example GitHub Actions workflow
- name: Run Code Review Agent
  run: python examples/test_agent.py --variant comprehensive-review
  
- name: Security Review
  run: python examples/test_agent.py --variant security-review
```

## Tips & Tricks

### 1. Review Production Code
```bash
# Read a file and pass it to the agent
$code = Get-Content src/main.py -Raw
python examples/test_agent.py --code $code
```

### 2. Batch Review Multiple Files
```python
import os
from pathlib import Path

for file in Path('src').glob('*.py'):
    code = file.read_text()
    print(f"\n\n=== Reviewing {file.name} ===")
    # Run agent with code
```

### 3. Compare Models
```bash
# Test with GPT-3.5 (faster, cheaper)
python examples/test_agent.py --model gpt-3.5-turbo

# Test with GPT-4 (smarter, more detailed)
python examples/test_agent.py --model gpt-4
```

## Customization

### Create Your Own Review Type

1. Create new prompt file:
   ```
   agents/code-review-assistant/user-prompt-performance-review.md
   ```

2. Update `config.json`:
   ```json
   {
     "name": "performance_review",
     "file": "user-prompt-performance-review.md",
     "description": "Review code for performance bottlenecks"
   }
   ```

3. Run it:
   ```bash
   python examples/test_agent.py --variant performance-review
   ```

## Cost Estimation

Using GPT-3.5-turbo (approximate):
- Input: ~0.0005 per 1K tokens
- Output: ~0.0015 per 1K tokens

**Example costs:**
- Quick review: ~$0.01-0.02
- Comprehensive review: ~$0.05-0.10
- Security review: ~$0.03-0.05

Use cheaper model for development, GPT-4 for final reviews.

---

For more examples and advanced usage, see:
- [Running and Testing Agents Guide](./running-and-testing-agents.md)
- [QUICK_START.md](./QUICK_START.md)
- [Main Documentation](../README.md)
