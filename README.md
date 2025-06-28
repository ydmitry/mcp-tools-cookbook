# FastMCP Hello World Example

A simple example project demonstrating how to build MCP (Model Context Protocol) tools using [FastMCP](https://github.com/jlowin/fastmcp), a fast, Pythonic framework for creating MCP servers and clients.

## 🚀 What is MCP?

The Model Context Protocol (MCP) is an open standard that enables secure, controlled access for AI applications to local and remote resources. FastMCP is a Python framework that makes it easy to build MCP servers and clients.

## 📋 Project Structure

```
mcp-tools-patterns/
├── requirements.txt          # Python dependencies
├── hello_world_server.py     # Main MCP server with tools, resources, and prompts
├── client_example.py         # Interactive client demo
├── simple_test.py            # Non-interactive test suite
├── test_setup.py             # Setup verification script
├── activate.sh               # Convenient virtual environment activation
├── venv/                     # Virtual environment (created after setup)
└── README.md                 # This file
```

## 🛠️ Features

This example server demonstrates the most basic MCP concept:

### 🔧 Tools
Functions that LLMs can call to perform actions:
- `hello_world(name)` - A simple greeting function that says hello to someone

## 🚀 Quick Start

### 1. Setup Virtual Environment and Install Dependencies

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

### 2. Run the Server

You can run the server in several ways:

#### Option A: Direct Python execution
```bash
python hello_world_server.py
```

#### Option B: Using FastMCP CLI (recommended)
```bash
fastmcp run hello_world_server.py
```

#### Option C: With custom transport (HTTP)
```bash
fastmcp run hello_world_server.py --transport http --port 8000
```

### 3. Test the Setup

First, verify everything is working:

```bash
python test_setup.py
```

Then run the comprehensive test:

```bash
python simple_test.py
```

### 4. Try the Interactive Client

Run the example client to see all features:

```bash
python client_example.py
```

Choose between:
- **Quick demo** (press Enter) - Basic hello world call
- **Full demo** (type 'full') - Multiple hello world examples

## 📖 Usage Examples

### Using the Client Programmatically

```python
import asyncio
from fastmcp import Client

async def example():
    client = Client("hello_world_server.py")
    
    async with client:
        # Call the hello_world tool with default name
        result = await client.call_tool("hello_world")
        print(result[0].text)  # "Hello, World! Welcome to FastMCP! 🚀"
        
        # Call the hello_world tool with custom name
        result = await client.call_tool("hello_world", {"name": "Alice"})
        print(result[0].text)  # "Hello, Alice! Welcome to FastMCP! 🚀"

asyncio.run(example())
```

### Using with LLM Applications

You can connect this server to LLM applications that support MCP:

1. **Claude Desktop**: Add to your MCP configuration
2. **Custom LLM apps**: Use the FastMCP client
3. **OpenAI integration**: Use FastMCP's OpenAI integration features

## 🔧 Development

### Adding New Tools

To add a new tool to the server:

```python
@mcp.tool
def your_new_tool(param1: str, param2: int = 0) -> str:
    """
    Description of what your tool does.
    
    Args:
        param1: Description of parameter 1
        param2: Description of parameter 2 (optional)
        
    Returns:
        Description of return value
    """
    # Your tool logic here
    return f"Result: {param1} + {param2}"
```

## 🌐 Advanced Usage

### HTTP Server Mode

Run as an HTTP server for remote access:

```bash
fastmcp run hello_world_server.py --transport http --port 8000
```

Then connect with:

```python
client = Client("http://localhost:8000")
```

### Server Configuration

You can configure the server with additional options:

```python
mcp = FastMCP(
    name="Your Server Name",
    instructions="Custom instructions for LLMs",
    # Add other configuration options
)
```

### Environment Variables

The server supports environment-based configuration. Create a `.env` file:

```env
MCP_SERVER_NAME=Hello World Server
MCP_LOG_LEVEL=INFO
```

## 📚 Learning More

### FastMCP Documentation
- [Official FastMCP Repository](https://github.com/jlowin/fastmcp)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp/tree/main/docs)

### MCP Specification
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)

### Key Concepts
- **Tools**: Functions that can be called by LLMs
- **Transports**: Communication methods (stdio, http, etc.)

## 🛠️ Troubleshooting

### Common Issues

1. **Import errors**: Make sure FastMCP is installed: `pip install fastmcp`
2. **Connection issues**: Ensure the server is running before starting the client
3. **Port conflicts**: If using HTTP transport, ensure the port is available

### Debug Mode

Run with debug logging:

```bash
fastmcp run hello_world_server.py --log-level DEBUG
```

### Inspecting the Server

Use the FastMCP inspect command to analyze your server:

```bash
fastmcp inspect hello_world_server.py
```

## 🤝 Contributing

This is a simple example project. To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with both server and client
5. Submit a pull request

## 📝 License

This example project is provided as-is for educational purposes. Check the FastMCP repository for its license terms.

## 🎯 Next Steps

After trying this example:

1. **Modify the tools** to do something useful for your use case
2. **Add authentication** if you need secure access
3. **Integrate with your LLM application** of choice
4. **Explore other FastMCP features** like middleware, composition, etc.
5. **Build more complex servers** with multiple tools and resources

Happy coding with FastMCP! 🚀 