#!/usr/bin/env python3
"""
Example client for interacting with the Hello World MCP Server.

This demonstrates how to:
- Connect to a FastMCP server
- Call tools
"""

import asyncio
from fastmcp import Client


async def demo_client():
    """Demonstrate interactions with the Hello World MCP Server."""
    
    # Create client pointing to our server script
    client = Client("mcp_server.py")
    
    print("🔌 Connecting to Hello World MCP Server...")
    
    async with client:
        # Test basic connection
        await client.ping()
        print("✅ Connected successfully!")
        print()
        
        # =============================================================================
        # LIST AVAILABLE CAPABILITIES
        # =============================================================================
        
        print("📋 Listing server capabilities...")
        
        # List available tools
        tools = await client.list_tools()
        print(f"🔧 Available tools ({len(tools)}):")
        for tool in tools:
            print(f"   - {tool.name}: {tool.description}")
        print()
        
        # =============================================================================
        # CALL TOOLS
        # =============================================================================
        
        print("🔧 Calling tools...")
        
        # Basic hello world with default name
        result = await client.call_tool("hello_world")
        print(f"hello_world(): {result[0].text}")
        
        # Hello world with custom name
        result = await client.call_tool("hello_world", {"name": "Alice"})
        print(f"hello_world('Alice'): {result[0].text}")
        
        # Another example
        result = await client.call_tool("hello_world", {"name": "FastMCP Developer"})
        print(f"hello_world('FastMCP Developer'): {result[0].text}")
        print()
        
        print("✨ Demo completed successfully!")


async def quick_demo():
    """A quick demonstration of the most basic functionality."""
    
    print("🚀 Quick Demo - Hello World MCP Client")
    print("=" * 50)
    
    client = Client("mcp_server.py")
    
    async with client:
        # Simple tool call
        result = await client.call_tool("hello_world", {"name": "FastMCP User"})
        print(f"📢 {result[0].text}")
    
    print("=" * 50)


if __name__ == "__main__":
    print("Choose demo mode:")
    print("1. Quick demo (press Enter)")
    print("2. Full demo (type 'full')")
    
    choice = input("Your choice: ").strip().lower()
    
    if choice == "full":
        asyncio.run(demo_client())
    else:
        asyncio.run(quick_demo()) 