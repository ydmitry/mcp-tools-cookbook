# MCP Tools Cookbook

A comprehensive collection of Model Context Protocol (MCP) tool patterns and recipes. This cookbook demonstrates various MCP design patterns that you can use as building blocks for your own AI-powered applications.

## 🧑‍🍳 Available Recipes (Patterns)

This cookbook demonstrates essential MCP tool patterns:

### 🎯 **Prompt Exposure Pattern**
- **`code_reviewer_prompt`** - Ready-to-use comprehensive code review prompts
- **`react_prompt_generator`** - Dynamic ReAct (Reason + Act) pattern prompt generation
- **Use case**: Transform MCP into a prompt repository service

### 🤔 **Clarification Questions Pattern**
- **`smart_recipe_generator`** - Progressive information gathering with intelligent questions
- **Use case**: Handle incomplete user input gracefully by asking targeted follow-up questions

### 🔄 **Multi-Step Tool Pattern**
- **`step1_initialize_workflow`** → **`step2_execute_workflow`** - Sequential tool dependencies
- **Use case**: Complex workflows requiring state management and ordered execution

### 🌐 **Client Tool Orchestration Pattern**
- **`sequential_web_search`** - Bridges external tools (like web_search) with MCP processing
- **Use case**: Extend and orchestrate native client tools from the server side

### 🎲 **Response-Driven Navigation Pattern**
- **`tool_with_follow_up`** - Tools that suggest next actions through embedded commands
- **`quantum_mood_analyzer`**, **`rubber_duck_debugger`**, **`coffee_brew_oracle`** - Fun example tools
- **Use case**: Guide conversation flow through tool response content

## 📸 Patterns in Action

See these MCP tool patterns demonstrated in real AI conversations:

### 🎯 Prompt Exposure Pattern
![Prompt Exposure Pattern](screenshots/prompt_exposure_tool_pattern.png)
*The `code_reviewer_prompt` tool exposing a comprehensive, ready-to-use code review template*

### 🤔 Clarification Questions Pattern
![Clarification Questions Pattern](screenshots/clarification_questions_pattern.png)
*The `smart_recipe_generator` tool progressively gathering information through targeted questions*

### 🌐 Client Tool Orchestration Pattern
![Client Tool Orchestration Pattern](screenshots/client_tool_orchestration_pattern.png)
*The `sequential_web_search` tool orchestrating multiple web searches and processing results*

### 🎲 Response-Driven Navigation Pattern
![Response-Driven Navigation Pattern](screenshots/response_driven_tool_navigation_pattern.png)
*The `tool_with_follow_up` tool suggesting next actions, leading to `rubber_duck_debugger` execution*

## 🚀 Quick Start

### Setup Your Kitchen (Environment)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Or use the convenient activation script:**
```bash
source activate.sh
```


## 📖 Recipe Examples

### Using with AI Applications

Connect this cookbook to LLM applications that support MCP:

1. **Claude Desktop**: Add to your MCP configuration
2. **Cursor**: Add to your MCP configuration
3. **Custom LLM apps**: Use the FastMCP client
4. **Other MCP clients**: Any MCP-compatible client can use these patterns

### Claude Desktop Configuration Example

```json
{
  "mcpServers": {
    "mcp-tools-cookbook": {
      "command": "python",
      "args": ["path-to-repository/mcp_server.py"]
    }
  }
}
```

### Cursor Configuration Example

Add to your `~/.cursor/mcp.json` file:

```json
{
  "mcp-tools-patterns": {
    "command": "python",
    "args": [
      "path-to-repository/mcp_server.py"
    ]
  }
}
```

## 🧑‍🍳 Creating Your Own Recipes

### Adding New Patterns

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

We welcome new MCP tool patterns! To contribute:

1. Fork the repository
2. Create a new pattern in the `patterns/` directory
3. Add comprehensive documentation and examples
4. Test your pattern thoroughly
5. Submit a pull request

### Pattern Contribution Guidelines

- **Clear documentation**: Explain the use case and implementation
- **Comprehensive examples**: Show how to use the pattern
- **Tests included**: Add test cases for your pattern
- **Follow conventions**: Use the established pattern structure

## 📝 License

This cookbook is provided as-is for educational purposes. Check the FastMCP repository for its license terms.

## 🎯 Next Steps

After exploring these patterns:

1. **Mix and match patterns** for your specific use cases
2. **Create hybrid patterns** combining multiple approaches
3. **Build production servers** using these patterns as foundations
4. **Share your own patterns** with the community
5. **Integrate with your favorite AI tools** and workflows

Happy cooking with MCP! 🚀🍳

---

*This cookbook demonstrates the versatility of the Model Context Protocol through practical, reusable patterns. Each pattern is a "recipe" you can adapt for your own AI-powered applications.* 
