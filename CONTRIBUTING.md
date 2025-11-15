# Contributing to AI Agents Prompts

Thank you for contributing to this repository! This document provides guidelines for adding or improving agents and prompts.

## How to Contribute

### Adding a New Agent

1. **Check for duplicates**: Review existing agents in `agents/` to avoid creating duplicates

2. **Create agent directory**:
   ```
   agents/your-agent-name/
   ```

3. **Create config.json**: Use `templates/agent-config-template.json` as a template

4. **Write system-prompt.md**: 
   - Use `templates/system-prompt-template.md` as reference
   - Reuse segments from `templates/reusable-segments.md` where applicable
   - Be specific about capabilities and constraints

5. **Create user prompts**: 
   - Create at least 2-3 `user-prompt-*.md` files
   - Each should target a specific use case
   - Use clear, descriptive filenames

6. **Document and test**: 
   - Update config.json with complete information
   - Test your agent prompts with real scenarios
   - Document any special setup or prerequisites

7. **Update main README.md**: 
   - Add your agent to the agent inventory table
   - Link to your agent directory

### Improving Existing Agents

1. **Identify improvements**: Test the agent and find what could be better

2. **Update the prompt**: Edit system or user prompts as needed

3. **Increment version**: Update version in config.json and file headers

4. **Document changes**: Add notes about what changed and why

5. **Test thoroughly**: Verify improvements work as expected

### Adding Reusable Segments

1. **Identify patterns**: Look for text used in multiple agents

2. **Extract and generalize**: Create a template with placeholders [like_this]

3. **Add to reusable-segments.md**: 
   - Use appropriate category or create new one
   - Include clear documentation
   - Provide usage examples

4. **Reference in agents**: Update config.json in agents using this segment

## Guidelines

### Agent Naming
- Use lowercase with hyphens: `my-agent-name`
- Be descriptive but concise
- Avoid generic names like "assistant" alone

### File Naming
- System prompts: `system-prompt.md`
- User prompts: `user-prompt-[purpose].md`
- Configuration: `config.json`
- Use lowercase with hyphens for file names

### Documentation Standards
- Write clear, accurate descriptions
- Include examples where helpful
- Document constraints and limitations
- Keep language professional but accessible

### Prompt Quality Checklist
- [ ] Clear role and identity defined
- [ ] Capabilities are specific and realistic
- [ ] Constraints and limitations documented
- [ ] Examples provided where appropriate
- [ ] Output format is clearly specified
- [ ] Tested with realistic scenarios
- [ ] Version number is appropriate

### Config.json Checklist
- [ ] All required fields completed
- [ ] Accurate version numbers
- [ ] All referenced files exist
- [ ] Tags are relevant and descriptive
- [ ] Notes explain any special requirements

## Version Numbering

Use semantic versioning: MAJOR.MINOR.PATCH

- **MAJOR**: Breaking changes (incompatible changes to behavior)
- **MINOR**: New features or significant improvements (backwards compatible)
- **PATCH**: Bug fixes and minor improvements

Examples:
- 1.0.0 → 1.1.0: Added new user prompt type
- 1.0.0 → 2.0.0: Changed core system prompt behavior
- 1.0.0 → 1.0.1: Fixed typo in instructions

## Testing Your Agent

Before submitting:

1. **Test basic functionality**: Does the agent behave as intended?
2. **Test edge cases**: What happens with unusual inputs?
3. **Test with examples**: Run through all user prompts
4. **Check formatting**: Is output properly formatted?
5. **Verify documentation**: Are all files complete and accurate?

## Commit Messages

When committing:

```
Add [agent-type]: Brief description

- What was added or changed
- Why this change was made
- Any important notes or decisions
```

Examples:
```
Add agent: Code Review Assistant

- New agent for code quality reviews
- Includes quick, comprehensive, and security-focused prompts
- Uses reusable segments for code quality standards
```

```
Improve: Technical Writer system prompt

- Enhanced API documentation section
- Added better examples
- Version bumped to 1.1.0
```

## Questions or Suggestions?

If you have questions about:
- **Prompt effectiveness**: Test and document your findings
- **Repository structure**: Propose changes with examples
- **New agent ideas**: Share the outcome you want to achieve
- **Reusable patterns**: Document where they're used

Add them to the repository as an issue or discussion.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Document your decisions
- Share knowledge and learnings
- Focus on improving prompt quality

---

Thank you for contributing! Your improvements make this repository more valuable for everyone. 🙏
