# Examples and Testing Guide

This folder contains examples and guides for running and testing the AI agents in this repository.

## 📚 Available Resources

### [Running and Testing AI Agents](./running-and-testing-agents.md)
**Complete guide on how to execute agents and test them** - Start here!

Includes:
- **Python examples** using OpenAI API
- **JavaScript/Node.js examples**
- **cURL examples** (no installation required)
- **Testing different agent variants** side-by-side
- **Best practices** for validation and monitoring
- **Troubleshooting** common issues

Quick example:
```python
# Load and run the Code Review Agent
system_prompt = load_prompt("agents/code-review-assistant/system-prompt.md")
user_prompt = load_prompt("agents/code-review-assistant/user-prompt-quick-review.md")
result = run_agent(system_prompt, user_prompt)
```

## 🎯 Example Use Cases

### Code Review Assistant
- **Quick Review**: Fast feedback during development
- **Comprehensive Review**: Thorough pre-merge analysis  
- **Security Review**: Security vulnerability scanning

### Technical Writer
- **API Documentation**: Generate API reference docs
- **Getting Started Guide**: Create onboarding documentation
- **Troubleshooting Guide**: Document common issues and solutions

## 📋 Examples to Add

Future examples you can contribute:
- **code-review-assistant-example**: Sample code with review feedback
- **technical-writer-example**: Example documentation output
- **prompt-customization**: How to customize prompts for specific needs
- **batch-testing**: How to test multiple agents in sequence
- **integration-example**: How to integrate agents into CI/CD pipelines

## 🚀 Getting Started

1. Read [Running and Testing AI Agents](./running-and-testing-agents.md)
2. Set up your API key (OpenAI, Azure, etc.)
3. Try the Python or JavaScript example
4. Customize with your own code/content
5. Test different agent variants

## 💡 Adding Your Own Examples

To contribute an example:

1. Create a subdirectory with a descriptive name
2. Include a README explaining the example
3. Document:
   - What agent and prompts were used
   - How to set up and run the example
   - Sample input and expected output
   - Lessons learned or best practices

Example structure:
```
examples/my-example/
├── README.md              # Explanation and instructions
├── input.txt              # Sample input data
├── expected_output.md     # Expected agent output
└── test_script.py         # Runnable test script
```
