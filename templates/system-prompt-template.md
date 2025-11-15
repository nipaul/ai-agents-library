# System Prompt Template

## Overview
A system prompt defines the core behavior, tone, and capabilities of an AI agent.

## Template Structure

### Role & Identity
```
You are a [specific role/agent name]. Your primary purpose is to [main objective].
```

### Core Capabilities
- List key functions the agent can perform
- Define boundaries and limitations
- Specify what the agent should NOT do

### Tone & Style
- Define communication style (formal, casual, technical, etc.)
- Specify language complexity level
- Detail any special formatting requirements

### Domain Expertise
- Define areas of expertise
- Specify knowledge cutoff or limitations
- Include relevant context or specialized terminology

### Instructions & Rules
1. Primary directive: [what must always be true]
2. Quality standards: [expected quality level]
3. Error handling: [how to handle edge cases]
4. Constraints: [hard limitations]

### Output Format
- Specify expected response format
- Include examples if applicable
- Define any special structures or templates

### Safety & Ethics
- Include content policy reminders
- Define what the agent should refuse
- Specify transparency requirements

---

## Example Minimal System Prompt
```
You are a [Agent Name]. Your role is to [primary function].

**Capabilities:**
- [capability 1]
- [capability 2]
- [capability 3]

**Communication Style:**
[description of tone and approach]

**Important Constraints:**
- [constraint 1]
- [constraint 2]

**Response Format:**
[specify how responses should be structured]
```

## Notes
- Keep system prompts focused and concise
- Test and iterate based on agent performance
- Document any custom instructions specific to your use case
