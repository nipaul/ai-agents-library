# AI Agents Prompts - Usage Guide

## Table of Contents
1. [Quick Reference](#quick-reference)
2. [How to Use an Existing Agent](#how-to-use-an-existing-agent)
3. [How to Create a New Agent](#how-to-create-a-new-agent)
4. [How to Add Reusable Segments](#how-to-add-reusable-segments)
5. [Versioning and Updates](#versioning-and-updates)
6. [Common Workflows](#common-workflows)

## Quick Reference

### File Locations
- **Agent templates**: `agents/[agent-name]/`
- **Prompt templates**: `templates/`
- **Reusable segments**: `templates/reusable-segments.md`
- **Documentation**: `docs/`

### Key Files in Each Agent
```
agents/my-agent/
├── config.json                    # Agent metadata
├── system-prompt.md              # Agent behavior definition
└── user-prompt-[purpose].md      # Specific use case prompts
```

## How to Use an Existing Agent

### Step 1: Review the Agent

Open the agent's `config.json` file to understand:
- What the agent does
- What versions exist
- What user prompts are available
- Any special tags or dependencies

**Example**: To use the Code Review Assistant:
```json
{
  "agent": {
    "name": "Code Review Assistant",
    "version": "1.0.0",
    "description": "AI agent specialized in reviewing code"
  },
  "user_prompts": [
    { "name": "quick_review", "file": "user-prompt-quick-review.md" },
    { "name": "comprehensive_review", "file": "user-prompt-comprehensive-review.md" }
  ]
}
```

### Step 2: Select a User Prompt

Choose the appropriate user prompt based on your need:
- **quick_review**: Fast feedback during development
- **comprehensive_review**: Thorough pre-merge review
- **security_review**: Security-focused analysis

### Step 3: Customize and Use

1. Open the user prompt file (e.g., `user-prompt-quick-review.md`)
2. Replace placeholders with your specific content
3. Follow the format and structure provided
4. Submit to the AI agent with the system prompt

### Example Workflow

**Goal**: Get a quick code review

1. **System Prompt**: Use `agents/code-review-assistant/system-prompt.md`
2. **User Prompt Template**: Use `agents/code-review-assistant/user-prompt-quick-review.md`
3. **Customize**:
   ```
   **Context:**
   I'm working on a user authentication module.

   **Task:**
   Please perform a quick code review focused on critical issues.

   **Code to Review:**
   \`\`\`python
   [Your code here]
   \`\`\`
   ```
4. **Submit**: Send both system and user prompts to your AI agent

## How to Create a New Agent

### Step 1: Plan Your Agent

Answer these questions:
- **What is the primary outcome?** (e.g., "Generate technical documentation")
- **What are the key capabilities?** (e.g., "Explain complex concepts, create examples")
- **Who is the audience?** (e.g., "Beginners, intermediate users")
- **What are the constraints?** (e.g., "Must be technical but accessible")

### Step 2: Create the Directory Structure

```powershell
# Create the agent directory
New-Item -ItemType Directory -Path "agents/my-new-agent"
```

### Step 3: Create config.json

Use `templates/agent-config-template.json` as a base:

```json
{
  "agent": {
    "name": "My New Agent",
    "version": "1.0.0",
    "description": "Brief description",
    "purpose": "Specific outcome",
    "created": "2025-11-14",
    "last_updated": "2025-11-14",
    "author": "Your Name",
    "tags": ["tag1", "tag2"]
  },
  "system_prompt": {
    "file": "system-prompt.md",
    "version": "1.0.0"
  },
  "user_prompts": [
    {
      "name": "primary_use_case",
      "file": "user-prompt-primary.md",
      "description": "Main use case",
      "use_case": "When to use",
      "version": "1.0.0"
    }
  ],
  "templates_used": [],
  "dependencies": [],
  "notes": "Any special notes"
}
```

### Step 4: Create system-prompt.md

Use `templates/system-prompt-template.md` as a starting point:

```markdown
You are [Agent Name], [role/identity]. Your primary purpose is to [main objective].

## Core Capabilities
- [capability 1]
- [capability 2]

## Tone & Style
[Describe how the agent should communicate]

## Key Instructions
1. [Important rule 1]
2. [Important rule 2]

## Response Format
[How responses should be structured]

## Important Constraints
- [Constraint 1]
- [Constraint 2]
```

**Tips**:
- Reference reusable segments from `templates/reusable-segments.md`
- Copy relevant segments directly into your system prompt
- Customize placeholder values for your agent
- Be specific about capabilities and constraints

### Step 5: Create User Prompts

For each use case, create a `user-prompt-[use-case].md`:

```markdown
**Context:**
[Background information]

**Task:**
[Specific objective]

**Format:**
[Expected output format]

**Additional Context:**
[Any relevant details]
```

Use `templates/user-prompt-template.md` as reference.

### Step 6: Document Reusable Segments

In your `config.json`, list which reusable segments you used:

```json
"templates_used": [
  "system-prompt-template.md",
  "reusable-segments.md (Code Quality Standard, Error Handling)"
]
```

## How to Add Reusable Segments

When you notice a pattern across multiple agents:

### Step 1: Identify the Pattern

Look for text that appears in multiple system prompts. Example:
```
When reviewing code, consider these aspects:
1. Correctness
2. Security
3. Performance
...
```

### Step 2: Extract and Generalize

Create a reusable version with placeholders:

```markdown
## My New Segment

When reviewing [ENTITY], consider these aspects:
1. [Aspect 1]
2. [Aspect 2]
...
```

### Step 3: Add to reusable-segments.md

1. Open `templates/reusable-segments.md`
2. Find the appropriate category or create a new one
3. Add your segment with:
   - Clear heading
   - Purpose explanation
   - Generic template with placeholders
   - Usage instructions

### Step 4: Update Agent Configs

In each agent that uses this segment:
1. Add the segment to their system prompt
2. Customize placeholders
3. Update `config.json` to reference it:
   ```json
   "templates_used": ["reusable-segments.md (My New Segment)"]
   ```

## Versioning and Updates

### Version Format

Use semantic versioning: `MAJOR.MINOR.PATCH`
- **MAJOR**: Breaking changes to prompt behavior
- **MINOR**: New capabilities or significant improvements
- **PATCH**: Minor improvements or fixes

### Updating an Agent

When you improve an agent:

1. **Update the file**: Modify `system-prompt.md` or `user-prompt-*.md`
2. **Increment version**: Update version in `config.json`
3. **Document changes**: Add notes about what changed
4. **Update timestamp**: Set `last_updated` to current date

Example:
```json
{
  "agent": {
    "version": "1.1.0"  // Updated
  },
  "system_prompt": {
    "version": "1.1.0"  // Updated
  },
  "notes": "Enhanced security review section with additional checks"
}
```

### Backwards Compatibility

- Keep old version numbers documented
- If making breaking changes, create a new agent or major version
- Clearly note what changed and why in the config

## Common Workflows

### Workflow 1: Quick Agent Reuse

**Goal**: Use an existing agent for a quick task

```
1. Open agents/[agent-name]/config.json
2. Choose appropriate user-prompt file
3. Customize with your content
4. Use with system-prompt.md
```

**Time**: 5-10 minutes

### Workflow 2: Create New Agent from Scratch

**Goal**: Build a new agent for a specific outcome

```
1. Plan the agent (role, capabilities, constraints)
2. Create directory structure
3. Copy and customize config.json
4. Write system prompt (use templates and segments)
5. Create 2-3 user prompts for common use cases
6. Test with real scenarios
7. Refine based on results
```

**Time**: 30-60 minutes

### Workflow 3: Refactor and Improve Existing Agent

**Goal**: Make an agent better based on usage

```
1. Identify what's working and what isn't
2. Extract successful patterns to reusable segments
3. Update system or user prompts
4. Increment version number
5. Document changes in config.json
6. Test improvements
7. Share learnings with team
```

**Time**: 20-45 minutes

### Workflow 4: Share New Reusable Pattern

**Goal**: Help other agents reuse a pattern you discovered

```
1. Identify pattern used in your agent
2. Generalize with placeholders
3. Add to templates/reusable-segments.md
4. Update your agent's config.json
5. Document which other agents could use it
6. Optional: Refactor those agents to use it
```

**Time**: 15-30 minutes

## Tips and Tricks

### When Customizing User Prompts
- Keep the structure but customize examples
- Preserve the context → task → format flow
- Add specific details that matter for your use case
- Reference the system prompt if additional context helps

### When Writing System Prompts
- Start specific, then broaden
- Test with edge cases and difficult scenarios
- Include explicit "don't do this" guidance
- Define success criteria clearly

### When Using Reusable Segments
- Don't copy-paste blindly
- Customize placeholder values [like this]
- Combine multiple segments if needed
- Document which segments you're using

### When Creating New Agents
- Start with 1-2 user prompts, add more as needed
- Use existing templates as inspiration
- Reuse segments when possible
- Version from 1.0.0, not 0.1.0

## Troubleshooting

### Agent behavior not as expected
1. Review the system prompt carefully
2. Check if user prompt is providing enough context
3. Add examples to the user prompt
4. Break complex tasks into multiple prompts

### Can't find appropriate agent
1. Check `agents/*/config.json` for tags
2. Review agent descriptions
3. Consider creating a new agent
4. Combine multiple agents if needed

### Prompt is too long
1. Use user prompts for variable content
2. Keep system prompts focused
3. Use reusable segments instead of inline examples
4. Consider breaking into multiple prompts

---

For more information, see the main [README.md](../README.md)
