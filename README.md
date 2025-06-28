# MCP Tools Cookbook

A comprehensive collection of Model Context Protocol (MCP) tool patterns and recipes. This cookbook demonstrates various MCP design patterns that you can use as building blocks for your own AI-powered applications.

## 🍳 What's Cooking?

The Model Context Protocol (MCP) is an open standard that enables secure, controlled access for AI applications to local and remote resources. This cookbook provides practical, ready-to-use patterns that demonstrate the full power of MCP through FastMCP, a fast, Pythonic framework for creating MCP servers and clients.

## 📋 Project Structure

```
mcp-tools-cookbook/
├── requirements.txt          # Python dependencies
├── mcp_server.py            # Main MCP server showcasing all patterns
├── client_example.py        # Interactive client demo
├── simple_test.py           # Test suite for all patterns
├── test_setup.py           # Setup verification script
├── activate.sh             # Virtual environment activation
├── patterns/               # Pattern implementations
│   ├── prompt_exposure_tool_pattern.py
│   ├── clarification_questions_pattern.py
│   ├── multi_step_tool_pattern.py
│   ├── react_prompt_exposure_pattern.py
│   ├── client_tool_orchestration_pattern.py
│   └── response_driven_tool_navigation_pattern.py
├── venv/                   # Virtual environment (created after setup)
└── README.md              # This cookbook guide
```

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

## 🚀 Quick Start

### 1. Setup Your Kitchen (Environment)

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

### 2. Start Cooking (Run the Server)

You can run the server in several ways:

#### Option A: Direct Python execution
```bash
python mcp_server.py
```

#### Option B: Using FastMCP CLI (recommended)
```bash
fastmcp run mcp_server.py
```

#### Option C: With custom transport (HTTP)
```bash
fastmcp run mcp_server.py --transport http --port 8000
```

### 3. Taste Test (Verify Setup)

First, verify everything is working:

```bash
python test_setup.py
```

Then run the comprehensive test:

```bash
python simple_test.py
```

### 4. Try the Interactive Demo

Run the example client to see all patterns in action:

```bash
python client_example.py
```

## 📖 Recipe Examples

### Using Pattern Tools Programmatically

```python
import asyncio
from fastmcp import Client

async def try_patterns():
    client = Client("mcp_server.py")
    
    async with client:
        # Try the code reviewer prompt pattern
        result = await client.call_tool("code_reviewer_prompt")
        print("Code Review Prompt:", result[0].text)
        
        # Try the clarification questions pattern
        result = await client.call_tool("smart_recipe_generator", 
                                      {"cuisine_type": "Italian"})
        print("Recipe Suggestion:", result[0].text)
        
        # Try the multi-step pattern
        workflow_result = await client.call_tool("step1_initialize_workflow", 
                                               {"workflow_name": "test-workflow"})
        print("Workflow Started:", workflow_result[0].text)

asyncio.run(try_patterns())
```

### Using with AI Applications

Connect this cookbook to LLM applications that support MCP:

1. **Claude Desktop**: Add to your MCP configuration
2. **Custom LLM apps**: Use the FastMCP client
3. **Other MCP clients**: Any MCP-compatible client can use these patterns

### Claude Desktop Configuration Example

```json
{
  "mcpServers": {
    "mcp-tools-cookbook": {
      "command": "python",
      "args": ["/path/to/mcp-tools-cookbook/mcp_server.py"],
      "env": {
        "PYTHONPATH": "/path/to/mcp-tools-cookbook"
      }
    }
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

## 🌐 Advanced Cooking Techniques

### HTTP Server Mode

Run as an HTTP server for remote access:

```bash
fastmcp run mcp_server.py --transport http --port 8000
```

### Environment Configuration

Create a `.env` file for environment-based configuration:

```env
MCP_SERVER_NAME=MCP Tools Cookbook
MCP_LOG_LEVEL=INFO
```

## 📚 Learning Resources

### FastMCP Documentation
- [Official FastMCP Repository](https://github.com/jlowin/fastmcp)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp/tree/main/docs)

### MCP Specification
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [MCP Servers Repository](https://github.com/modelcontextprotocol/servers)

### Key Concepts
- **Tools**: Functions that can be called by LLMs
- **Patterns**: Reusable design approaches for different use cases
- **Transports**: Communication methods (stdio, http, etc.)

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
