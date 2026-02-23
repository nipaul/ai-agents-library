# AI Agents Prompts Repository

A structured collection of system and user prompts for outcome-specific AI agents. This repository serves as a library of prompt configurations that can be reused, refined, and adapted for various AI agent implementations.

## 📋 Overview

This repository organizes AI agent prompts into a standardized structure, making it easy to:
- **Create** new agents with consistent patterns
- **Manage** prompts and their versions
- **Reuse** common prompt segments across agents
- **Document** agent behavior and capabilities
- **Refactor** and improve prompts iteratively

## 🗂️ Repository Structure

```
ai-agents-prompts/
├── agents/                          # Agent-specific prompt files
│   ├── code-review-assistant/       # Example: Code review agent
│   │   ├── config.json             # Agent metadata and configuration
│   │   ├── system-prompt.md        # System prompt defining agent behavior
│   │   ├── user-prompt-quick-review.md
│   │   ├── user-prompt-comprehensive-review.md
│   │   └── user-prompt-security-review.md
│   ├── technical-writer/            # Example: Technical writing agent
│   │   ├── config.json
│   │   ├── system-prompt.md
│   │   ├── user-prompt-api-docs.md
│   │   ├── user-prompt-getting-started.md
│   │   └── user-prompt-troubleshooting.md
│   └── [other-agent]/
├── templates/                       # Reusable templates and segments
│   ├── system-prompt-template.md   # Template for creating system prompts
│   ├── user-prompt-template.md     # Template for creating user prompts
│   ├── agent-config-template.json  # Template for agent configuration
│   └── reusable-segments.md        # Common prompt sections
├── examples/                        # Usage examples and samples
├── docs/                           # Detailed documentation
│   └── USAGE_GUIDE.md
└── README.md                       # This file
```

## 🚀 Quick Start

### Working With This Repo

Before making changes, read `AGENTS.md` for repository-specific guidance on structure, naming, and update workflow.

### Adding a New Agent

1. **Create a new directory** in `agents/`:
   ```
   agents/my-new-agent/
   ```

2. **Copy the templates**:
   - `config.json` from `templates/agent-config-template.json`
   - `system-prompt.md` from `templates/system-prompt-template.md`

3. **Create user prompts** for specific use cases:
   - Use `templates/user-prompt-template.md` as a guide
   - Name them descriptively: `user-prompt-[use-case].md`

4. **Fill in the metadata** in `config.json`:
   - Agent name, version, description
   - Reference to system prompt file
   - List of user prompt files
   - Tags and dependencies

5. **Use reusable segments** from `templates/reusable-segments.md`:
   - Copy relevant segments into your system prompt
   - Customize placeholders for your specific agent

### Using an Existing Agent

Each agent directory contains:
- **config.json**: Overview and file references
- **system-prompt.md**: Define the agent's behavior once
- **user-prompt-*.md**: Different prompts for specific use cases

To use an agent:
1. Review the `config.json` to understand the agent's purpose
2. Read the `system-prompt.md` to set up the agent
3. Choose the appropriate `user-prompt-*.md` file for your use case
4. Customize with your specific details

### 🏃 Running and Testing Agents

To actually **run and test** agents with AI models:

**📖 Start with the [Running and Testing Agents Guide](./examples/running-and-testing-agents.md)** - it includes:
- Python and JavaScript code examples
- Setup instructions for OpenAI API and other services
- How to test different agent variants
- Best practices for validation and monitoring
- Troubleshooting common issues

**⚡ Quick Start** (60 seconds):
1. Install: `pip install openai`
2. Set API key: `$env:OPENAI_API_KEY="your-key"`
3. Run: `python examples/test_agent.py`

See [examples/QUICK_START.md](./examples/QUICK_START.md) for common commands and examples.

## 📄 File Types

### System Prompts (`system-prompt.md`)
Defines the core behavior, capabilities, and personality of an agent. Should include:
- Role and identity
- Core capabilities
- Tone and style
- Domain expertise
- Key instructions and rules
- Output format specifications
- Safety and ethics guidelines

**Example**: `agents/code-review-assistant/system-prompt.md`

### User Prompts (`user-prompt-*.md`)
Specific requests or interactions sent to an agent for particular outcomes. Should include:
- Context setup
- Specific task or request
- Expected output format
- Optional examples
- Relevant constraints

**Example**: `agents/code-review-assistant/user-prompt-quick-review.md`

### Agent Configuration (`config.json`)
Metadata about an agent, including:
- Agent identity (name, version, description, purpose)
- System prompt reference
- List of user prompts with descriptions
- Templates and segments used
- Dependencies and special notes

**Example**: `agents/code-review-assistant/config.json`

### Reusable Segments (`reusable-segments.md`)
Common prompt sections that appear in multiple agents:
- Code quality standards
- Error handling patterns
- Analysis frameworks
- Documentation patterns
- Test case templates
- Output formatting guidelines

Use these to maintain consistency across agents and reduce duplication.

## 🔄 Workflow: Adding and Refactoring

### Creating a New Agent

```
1. Define the outcome/purpose
   ├─ What specific result should this agent achieve?
   └─ What skills or expertise does it need?

2. Create agent directory structure
   ├─ agents/[agent-name]/
   ├─ config.json
   ├─ system-prompt.md
   └─ user-prompt-*.md

3. Write system prompt
   ├─ Use system-prompt-template.md as reference
   ├─ Define role, capabilities, tone
   └─ Incorporate relevant reusable segments

4. Create user prompts
   ├─ Identify different use cases
   ├─ Create user-prompt for each use case
   └─ Include examples where helpful

5. Iterate and refactor
   ├─ Test with real prompts
   ├─ Refine based on results
   └─ Update version in config.json
```

### Refactoring Existing Agents

When improving an agent:

1. **Identify patterns** across agents that could be reusable
2. **Extract to segments** in `templates/reusable-segments.md`
3. **Update agents** to reference the shared segment
4. **Version tracking**:
   - Update version numbers in `config.json`
   - Document changes in agent notes
   - Keep old versions as comments if needed

## 🔗 Reusing and Sharing

### Using Reusable Segments

1. Browse `templates/reusable-segments.md`
2. Find the segment that fits your need
3. Copy into your system prompt
4. Customize placeholder values [like this]
5. Update your `config.json` to document which segments you used

### Creating New Segments

When you notice a pattern appearing in multiple agents:

1. Extract the common text
2. Identify customizable parts
3. Add to `templates/reusable-segments.md`
4. Document the use cases
5. Update agent configs that could use it

## 📊 Agent Inventory

Current agents in this repository:

| Agent | Purpose | User Prompts | Status |
|-------|---------|--------------|--------|
| **Code Review Assistant** | Provide thorough code reviews | 3 (Quick, Comprehensive, Security) | ✅ Example |
| **Technical Writer** | Create technical documentation | 3 (API Docs, Getting Started, Troubleshooting) | ✅ Example |
| [Your Agent] | [Description] | [Count] | [Status] |

## 💡 Best Practices

### When Writing System Prompts
- Be clear and specific about the agent's role
- Include what the agent should NOT do
- Define output formats explicitly
- Use examples for complex behaviors
- Keep prompts focused and concise

### When Writing User Prompts
- Provide necessary context
- Be specific about the task
- Specify output format clearly
- Include examples for complex requests
- One prompt per specific use case

### General Guidelines
- **Version everything**: Track changes in config.json
- **Document decisions**: Use the "notes" field in config.json
- **Reuse segments**: Share common patterns via templates
- **Test thoroughly**: Try prompts with real scenarios
- **Iterate**: Refactor as you learn what works

## 🔧 Configuration Format

Each agent includes a `config.json` file:

```json
{
  "agent": {
    "name": "Agent Name",
    "version": "1.0.0",
    "description": "What the agent does",
    "purpose": "The specific outcome it achieves",
    "created": "YYYY-MM-DD",
    "last_updated": "YYYY-MM-DD",
    "author": "Your Name",
    "tags": ["tag1", "tag2"]
  },
  "system_prompt": {
    "file": "system-prompt.md",
    "version": "1.0.0"
  },
  "user_prompts": [
    {
      "name": "prompt_identifier",
      "file": "user-prompt-name.md",
      "description": "What this prompt does",
      "use_case": "When to use this",
      "version": "1.0.0"
    }
  ],
  "templates_used": ["template-name"],
  "notes": "Any additional information"
}
```

## 📈 Next Steps

- Review existing agents in `agents/`
- Read through `templates/` to understand patterns
- Create your first custom agent
- Contribute improvements via pull requests
- Document learnings and refactor as needed

## 📚 Additional Resources

- [System Prompt Template](templates/system-prompt-template.md)
- [User Prompt Template](templates/user-prompt-template.md)
- [Reusable Segments](templates/reusable-segments.md)
- [Usage Guide](docs/USAGE_GUIDE.md)

## 📝 Notes

This repository is designed to be **iterative and collaborative**. As you build and use agents:
- Refactor prompts based on real-world results
- Extract common patterns into reusable segments
- Document what works and what doesn't
- Share improvements with the team

Happy prompt engineering! 🚀
