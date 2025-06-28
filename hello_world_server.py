#!/usr/bin/env python3
"""
A simple FastMCP server with a hello world tool.

This demonstrates basic FastMCP functionality with:
- Tools: Functions that can be called by LLMs
"""

from fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP(
    name="Hello World MCP Server",
    instructions="""
    This is a simple demonstration server that provides a basic greeting functionality.
    Use the hello_world tool to get personalized greetings.
    """
)

# =============================================================================
# TOOLS - Functions that LLMs can call
# =============================================================================

@mcp.tool
def hello_world(name: str = "World") -> str:
    """
    A simple greeting tool that says hello to someone.
    
    Args:
        name: The name of the person to greet (defaults to "World")
    
    Returns:
        A personalized greeting message
    """
    return f"Hello, {name}! Welcome to FastMCP! 🚀"

# =============================================================================
# MAIN - Server execution
# =============================================================================

if __name__ == "__main__":
    print("🚀 Starting Hello World MCP Server...")
    print("📡 Available endpoints:")
    print("   Tools: hello_world")
    print("\n💡 Run with: fastmcp run hello_world_server.py")
    print("   Or directly: python hello_world_server.py")
    print()
    
    # Run the server (default: stdio transport)
    mcp.run() 