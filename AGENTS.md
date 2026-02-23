# AGENTS.md

Guidance for AI agents working in this repository.

## What This Repo Is
A structured library of AI agent prompts. Each agent lives under `agents/<agent-name>/` and is composed of a `config.json`, a `system-prompt.md`, and one or more `user-prompt-*.md` files.

## Golden Rules
- Preserve the repository structure and naming conventions.
- Prefer editing existing templates and reusable segments over duplicating content.
- Keep prompts concise, explicit, and outcome-focused.
- Use ASCII unless the file already contains non-ASCII.

## Where Things Live
- `agents/`: agent definitions and prompts
- `templates/`: prompt templates and `reusable-segments.md`
- `docs/`: usage documentation
- `examples/`: runnable examples and quick starts

## Adding or Updating an Agent
1. Create or update `agents/<agent-name>/`.
2. Use templates:
   - `templates/agent-config-template.json`
   - `templates/system-prompt-template.md`
   - `templates/user-prompt-template.md`
3. Required files per agent:
   - `config.json`
   - `system-prompt.md`
   - `user-prompt-*.md` (at least 2 when adding a new agent)
4. Update `config.json` with:
   - semantic version bump
   - `last_updated` date (YYYY-MM-DD)
   - accurate file references and notes
5. If you create reusable patterns, add them to `templates/reusable-segments.md` and reference them in `config.json`.

## Naming Conventions
- Agent directories: lowercase with hyphens (`agents/code-review-assistant/`).
- Prompts: `system-prompt.md` and `user-prompt-<purpose>.md`.
- Keep purpose names short and specific.

## Quality Checklist
- Role, capabilities, and constraints are explicit.
- Output format is clearly specified.
- Prompts are tested with realistic inputs.
- Examples are included when the task is non-trivial.

## Documentation Updates
- If you add a new agent, update the agent inventory in `README.md`.
- Keep `docs/USAGE_GUIDE.md` aligned with any workflow changes.

## Tests
There are no automated tests. Validate by manually running prompts or following `examples/running-and-testing-agents.md`.