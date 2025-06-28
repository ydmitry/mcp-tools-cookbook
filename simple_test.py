#!/usr/bin/env python3
"""
Simple non-interactive test to demonstrate FastMCP client functionality.
"""

import asyncio
from fastmcp import Client


async def simple_test():
    """Run a simple test of the Hello World MCP Server."""
    
    print("🚀 FastMCP Hello World Test")
    print("=" * 40)
    
    # Create client pointing to our server script
    client = Client("mcp_server.py")
    
    try:
        async with client:
            print("✅ Connected to server")
            
            # Test basic tool call with default parameter
            print("\n🔧 Testing hello_world tool (default):")
            result = await client.call_tool("hello_world")
            print(f"   Result: {result[0].text}")
            
            # Test tool call with custom name
            print("\n🔧 Testing hello_world tool (with name):")
            result = await client.call_tool("hello_world", {"name": "FastMCP User"})
            print(f"   Result: {result[0].text}")
            
            # Test with another name
            print("\n🔧 Testing hello_world tool (another example):")
            result = await client.call_tool("hello_world", {"name": "Developer"})
            print(f"   Result: {result[0].text}")
            
            print("\n✨ All tests completed successfully!")
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    
    return True


if __name__ == "__main__":
    success = asyncio.run(simple_test())
    if success:
        print("\n🎉 FastMCP Hello World example is working perfectly!")
        print("\n📋 What you can do next:")
        print("   • Run: python mcp_server.py")
        print("   • Try: fastmcp run mcp_server.py")
        print("   • Modify the tool in mcp_server.py")
        print("   • Connect this server to Claude Desktop or other MCP clients")
    else:
        print("\n❌ Some tests failed. Check the server configuration.")
        exit(1) 