# How to Contribute

We welcome new MCP tool patterns! This guide will help you contribute your own patterns to the MCP Tools Cookbook.

## 🧑‍🍳 Creating New Recipes

### Recipe Design Philosophy

Think of each MCP tool pattern as a "recipe" that solves a specific interaction challenge between AI systems and users. A good recipe should:

- **Solve a real problem**: Address a common pain point in AI interactions
- **Be reusable**: Work across different use cases and applications
- **Demonstrate a clear pattern**: Show a technique others can adapt
- **Provide excellent UX**: Make AI interactions smoother and more intuitive

### Recipe Ideation Process

#### 1. Identify the Problem
Start by observing friction points in AI interactions:
- What do users struggle with when using AI tools?
- Where do current tools fail or feel clunky?
- What manual processes could be automated?
- How can we make AI more helpful and context-aware?

#### 2. Choose Your Pattern Type

**🎯 Prompt Exposure Patterns**
- Transform MCP into a prompt repository
- Expose ready-to-use, high-quality prompts
- Examples: Code review templates, writing assistants

**🤔 Clarification Patterns**
- Handle incomplete user input gracefully
- Ask intelligent follow-up questions
- Progressive information gathering
- Examples: Smart forms, guided workflows

**🔄 Multi-Step Patterns**
- Complex workflows requiring state management
- Sequential tool dependencies
- Ordered execution patterns
- Examples: Deployment pipelines, data processing workflows

**🌐 Orchestration Patterns**
- Bridge external tools with MCP processing
- Extend native client capabilities
- Coordinate multiple services
- Examples: API integrations, service coordination

**🎲 Navigation Patterns**
- Guide conversation flow through responses
- Suggest next actions dynamically
- Create engaging interaction loops
- Examples: Interactive tutorials, exploration tools

#### 3. Design Your Recipe

**Core Questions to Answer:**
- What specific problem does this solve?
- Who is the target user?
- What's the expected workflow?
- How does it improve the user experience?
- What makes it reusable?

**Recipe Structure:**
```python
# Clear, descriptive name
def your_recipe_name():
    """
    Brief description of what problem this solves
    and what pattern it demonstrates.
    """
    # Implementation that others can understand and adapt
```

### 🍳 Recipe Examples by Pattern

#### Example: Information Gathering Recipe
```python
@mcp.tool
def smart_form_builder(
    form_type: str,
    user_response: str = None,
    session_id: str = "default"
) -> str:
    """
    CLARIFICATION QUESTIONS PATTERN: Builds forms by asking smart questions.
    
    Demonstrates progressive information gathering with context awareness.
    """
    # Pattern: Ask one question at a time, remember context
    # Use case: Any scenario requiring structured input
```

#### Example: Workflow Orchestration Recipe
```python
@mcp.tool
def deployment_orchestrator(
    step: str,
    environment: str,
    previous_result: str = None
) -> str:
    """
    MULTI-STEP PATTERN: Orchestrates complex deployment workflows.
    
    Demonstrates state management across multiple operations.
    """
    # Pattern: Sequential steps with state persistence
    # Use case: Any multi-step process requiring coordination
```

## 🛠️ Adding New Patterns

To add a new tool pattern to the cookbook:

1. **Create a new pattern file** in the `patterns/` directory:

```python
# patterns/your_new_pattern.py
from fastmcp import FastMCP

def register_your_pattern_tools(mcp: FastMCP):
    """Register your new pattern tools with the MCP server"""
    
    @mcp.tool
    def your_pattern_tool(param1: str, param2: int = 0) -> str:
        """
        Description of your pattern and what it demonstrates.
        
        Args:
            param1: Parameter description
            param2: Optional parameter description
            
        Returns:
            Description of return value
        """
        # Your pattern implementation here
        return f"Pattern result: {param1} + {param2}"
```

2. **Register it in the main server** (`mcp_server.py`):

```python
from patterns.your_new_pattern import register_your_pattern_tools

# Register your pattern
register_your_pattern_tools(mcp)
```

## 🛠️ Troubleshooting

### Common Issues

1. **Import errors**: Make sure FastMCP is installed: `pip install fastmcp`
2. **Connection issues**: Ensure the server is running before starting the client
3. **Port conflicts**: If using HTTP transport, ensure the port is available
4. **Pattern not working**: Check the specific pattern documentation in the `patterns/` directory

### Debug Mode

Run with debug logging:

```bash
fastmcp run mcp_server.py --log-level DEBUG
```

### Inspecting the Server

Use the FastMCP inspect command to analyze your server:

```bash
fastmcp inspect mcp_server.py
```

## 🤝 Contributing New Recipes

To contribute a new pattern:

1. **Fork the repository**
2. **Create a new pattern in the `patterns/` directory**
3. **Add comprehensive documentation and examples**
4. **Test your pattern thoroughly**
5. **Submit a pull request**

### Pattern Contribution Guidelines

When contributing a new pattern, please ensure:

- **Clear documentation**: Explain the use case and implementation
- **Comprehensive examples**: Show how to use the pattern
- **Tests included**: Add test cases for your pattern
- **Follow conventions**: Use the established pattern structure

### Step-by-Step Contribution Process

#### 1. Setting Up Your Development Environment

```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/mcp-tools-patterns.git
cd mcp-tools-patterns

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 2. Creating Your Pattern

Create a new pattern file in the `patterns/` directory:

```python
# patterns/your_new_pattern.py
from fastmcp import FastMCP

def register_your_pattern_tools(mcp: FastMCP):
    """Register your new pattern tools with the MCP server"""
    
    @mcp.tool
    def your_pattern_tool(param1: str, param2: int = 0) -> str:
        """
        Description of your pattern and what it demonstrates.
        
        Args:
            param1: Parameter description
            param2: Optional parameter description
            
        Returns:
            Description of return value
        """
        # Your pattern implementation here
        return f"Pattern result: {param1} + {param2}"
```

#### 3. Registering Your Pattern

Add your pattern to the main server (`mcp_server.py`):

```python
from patterns.your_new_pattern import register_your_pattern_tools

# Register your pattern
register_your_pattern_tools(mcp)
```

#### 4. Testing Your Pattern

- Test your pattern thoroughly with different inputs
- Ensure it follows the established conventions
- Add test cases if applicable
- Verify it works with MCP clients

#### 5. Documentation

- Document your pattern's use case clearly
- Provide examples of how to use it
- Explain the implementation approach
- Add screenshots if helpful

#### 6. Submitting Your Pull Request

1. Create a descriptive branch name: `git checkout -b add-your-pattern-name`
2. Commit your changes with clear messages
3. Push to your fork
4. Create a pull request with:
   - Clear title describing the pattern
   - Detailed description of the use case
   - Examples of usage
   - Any relevant screenshots

## 📋 Pattern Quality Checklist

Before submitting, ensure your pattern meets these criteria:

- [ ] **Functionality**: Pattern works as intended
- [ ] **Documentation**: Clear explanation of use case and implementation
- [ ] **Examples**: Practical usage examples provided
- [ ] **Testing**: Pattern has been tested with MCP clients
- [ ] **Code Quality**: Clean, readable, and well-commented code
- [ ] **Convention Compliance**: Follows established project patterns
- [ ] **Error Handling**: Appropriate error handling where needed

## 🎯 Types of Contributions Welcome

We're looking for patterns that demonstrate:

- **Novel interaction patterns** with AI systems
- **Integration approaches** with external services
- **State management techniques** for complex workflows
- **User experience improvements** for AI interactions
- **Creative uses** of MCP capabilities

## 💡 Need Help?

If you need assistance with your contribution:

1. Check existing patterns for reference
2. Open an issue to discuss your idea
3. Ask questions in pull request discussions
4. Review the FastMCP documentation

Thank you for contributing to the MCP Tools Cookbook! 🍳 