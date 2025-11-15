# Examples Index

Complete guide to running and testing AI agents from this repository.

## 📚 Documentation Files

### [QUICK_START.md](./QUICK_START.md) ⭐ **Start Here**
- 60-second setup guide
- Common commands and usage
- Troubleshooting for common issues
- **Best for**: Getting up and running quickly

### [running-and-testing-agents.md](./running-and-testing-agents.md) 📖 **Complete Guide**
- Detailed setup instructions
- Python examples (OpenAI API)
- JavaScript/Node.js examples
- cURL examples (no installation needed)
- Testing different agents and variants
- Best practices and patterns
- API usage tracking and monitoring
- **Best for**: Understanding all the details

### [example-code-review.md](./example-code-review.md) 🎯 **Real-World Example**
- Complete code review walkthrough
- Sample input code
- Output from all 3 review variants (Quick, Comprehensive, Security)
- Comparison table
- Integration examples (CI/CD, pre-commit hooks)
- Tips and tricks
- Cost estimation
- **Best for**: Seeing real examples of agent output

### [README.md](./README.md) 📋 **Overview**
- Summary of available resources
- Example use cases
- How to contribute examples
- **Best for**: Navigation and overview

---

## 🛠️ Executable Scripts

### [test_agent.py](./test_agent.py) 🐍 **Python Runner**
Complete Python script to run any agent with various options.

**Usage:**
```bash
python test_agent.py                          # Run default example
python test_agent.py --list                   # List agents
python test_agent.py --info code-review-assistant
python test_agent.py --agent technical-writer --variant api-docs
python test_agent.py --code "def hello(): pass"
python test_agent.py --model gpt-4            # Use GPT-4
```

**Features:**
- List available agents
- Show agent details
- Test specific variants
- Pass custom code
- Select different models
- Error handling and helpful messages

---

## 🎓 Learning Path

### For New Users
1. **First**: Read [QUICK_START.md](./QUICK_START.md) (5 minutes)
2. **Second**: Run `python test_agent.py` (2 minutes)
3. **Third**: Read [example-code-review.md](./example-code-review.md) (10 minutes)

### For Detailed Understanding
1. Read [running-and-testing-agents.md](./running-and-testing-agents.md)
2. Try all the code examples (Python, JavaScript, cURL)
3. Run different agent variants
4. Customize for your use cases

### For Integration
1. Review [example-code-review.md](./example-code-review.md) integration section
2. Set up pre-commit hooks or CI/CD
3. Customize agents from `templates/`

---

## 🚀 Quick Reference

### Setup
```bash
pip install openai
$env:OPENAI_API_KEY="sk-..."
```

### Run Agents
```bash
# Code Review Agent
python test_agent.py                          # Quick review (default)
python test_agent.py --variant comprehensive-review
python test_agent.py --variant security-review

# Technical Writer Agent
python test_agent.py --agent technical-writer --variant api-docs
python test_agent.py --agent technical-writer --variant getting-started
python test_agent.py --agent technical-writer --variant troubleshooting

# List all agents
python test_agent.py --list

# Show agent info
python test_agent.py --info code-review-assistant
```

### Custom Code
```bash
# Review your own code
python test_agent.py --code "def hello(): return True"

# Use GPT-4 instead of GPT-3.5
python test_agent.py --model gpt-4
```

---

## 📊 Example Outputs

See [example-code-review.md](./example-code-review.md) for:
- Sample Python code
- Quick review output
- Comprehensive review output
- Security-focused review output
- Refactored code examples
- Security improvements

---

## 🎯 Use Cases

### During Development
→ Use **Quick Review** variant for fast feedback on work-in-progress code

### Before Merging
→ Use **Comprehensive Review** variant for thorough pre-merge analysis

### Security Audits
→ Use **Security Review** variant to identify vulnerabilities

### API Documentation
→ Use **Technical Writer** agent with api-docs variant

### Getting Started Guides
→ Use **Technical Writer** agent with getting-started variant

### Troubleshooting Documentation
→ Use **Technical Writer** agent with troubleshooting variant

---

## 💡 Tips

### Performance
- Use `gpt-3.5-turbo` for quick feedback (cheaper)
- Use `gpt-4` for final reviews (smarter)

### Batch Testing
```python
# Test multiple files
for file in Path('src').glob('*.py'):
    os.system(f"python test_agent.py --code '{file.read_text()}'")
```

### Custom Agents
- Copy templates from `templates/`
- Create new variants in `agents/`
- Update `config.json`

### API Key Management
- **Development**: Use environment variable
- **Production**: Use secrets management service
- **CI/CD**: Use GitHub Secrets or equivalent

---

## 📖 Related Documentation

- [Main README.md](../README.md) - Overview and structure
- [USAGE_GUIDE.md](../docs/USAGE_GUIDE.md) - Detailed workflows
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Contribution guidelines
- [Templates](../templates/) - Reusable prompt templates

---

## ❓ Troubleshooting

### Common Issues

**"OPENAI_API_KEY not found"**
```powershell
$env:OPENAI_API_KEY="sk-your-key"
```

**"ModuleNotFoundError: No module named 'openai'"**
```bash
pip install openai
```

**"Invalid API key"**
- Verify key at https://platform.openai.com/api-keys
- Key might be expired
- Try re-setting the environment variable

**"Rate limit exceeded"**
- Wait a minute and retry
- Upgrade to paid API plan if needed

**"Agent not found"**
```bash
python test_agent.py --list  # See available agents
```

For more help, see:
- [Troubleshooting section in running-and-testing-agents.md](./running-and-testing-agents.md#troubleshooting)
- [QUICK_START.md troubleshooting](./QUICK_START.md#troubleshooting)

---

## 🤝 Contributing

To add your own examples:
1. Create a subdirectory with a descriptive name
2. Include a README explaining the example
3. Document setup, usage, and output
4. Add to this index

See [README.md](./README.md) for details.

---

## 📈 Next Steps

1. ✅ Run your first agent with `python test_agent.py`
2. ✅ Review the output and example codes
3. ✅ Customize prompts for your use cases
4. ✅ Create new agents from templates
5. ✅ Integrate into your workflow
6. ✅ Share improvements with the team

Happy prompting! 🚀
