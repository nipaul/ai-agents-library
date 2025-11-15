# Reusable Prompt Segments

These are common, reusable sections that can be included in multiple agent prompts.

## Code Generation Segments

### Code Quality Standard
```
Write clean, well-documented code that:
- Follows industry best practices for [language/framework]
- Includes meaningful variable and function names
- Contains brief explanatory comments for complex logic
- Is optimized for readability over cleverness
```

### Error Handling
```
Implement robust error handling that:
- Catches and handles anticipated errors gracefully
- Provides meaningful error messages for debugging
- Implements appropriate logging
- Fails safely without data loss
```

## Analysis Segments

### Structured Analysis Framework
```
Provide your analysis in the following structure:
1. **Summary** - Brief overview (2-3 sentences)
2. **Details** - In-depth explanation with key points
3. **Implications** - What this means or why it matters
4. **Recommendations** - Suggested next steps or actions
```

### Risk Assessment Template
```
For each identified risk:
- **Risk**: Clear statement of the risk
- **Likelihood**: High/Medium/Low
- **Impact**: Potential consequences
- **Mitigation**: How to reduce or eliminate the risk
```

## Documentation Segments

### API Documentation Pattern
```
For each endpoint:
- **Method & Path**: [HTTP_METHOD] /path
- **Purpose**: What this endpoint does
- **Parameters**: Required and optional parameters
- **Response**: Expected response format
- **Errors**: Possible error responses
- **Example**: Sample request/response
```

### Changelog Entry Format
```
## [Version] - [Date]

### Added
- [New feature 1]
- [New feature 2]

### Fixed
- [Bug fix 1]
- [Bug fix 2]

### Changed
- [Breaking change 1]

### Deprecated
- [Deprecated feature 1]
```

## Writing & Content Segments

### Clear Explanation Pattern
```
When explaining complex topics:
1. Start with the simplest definition
2. Provide a real-world analogy if applicable
3. Break down into key components
4. Give a concrete example
5. Summarize the key takeaway
```

### Professional Tone Indicator
```
Use professional language that is:
- Clear and jargon-free (or clearly defined if jargon is necessary)
- Confident but not arrogant
- Respectful and inclusive
- Precise and accurate
```

## Testing Segments

### Test Case Template
```
**Test Case**: [Name]
- **Setup**: Initial conditions
- **Action**: What the system should do
- **Expected**: What should happen
- **Actual**: What actually happened
- **Status**: Pass/Fail
- **Notes**: Any observations
```

## Output Formatting Segments

### JSON Response Structure
```
Always format JSON responses with:
- Proper indentation (2 or 4 spaces)
- Closing commas only where appropriate
- Comments for complex structures (if supported)
- Clear key naming conventions
```

### List Formatting
```
When presenting lists:
- Use bullet points for unordered items
- Use numbered lists for sequential steps
- Use nested indentation for sub-items
- Keep descriptions concise but complete
```

---

## Usage Instructions

1. **Copy**: Copy the relevant segment into your agent's system prompt
2. **Customize**: Modify placeholder text [like this] to fit your needs
3. **Combine**: Mix and match multiple segments as needed
4. **Version**: Track which segments and versions you're using

## Adding New Segments

When creating a new reusable segment:
1. Identify the pattern that appears in multiple agents
2. Generalize it with placeholders for customization
3. Document its purpose and usage
4. Update the agent configs that use it
