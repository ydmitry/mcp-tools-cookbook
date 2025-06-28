#!/usr/bin/env python3
"""
Simple test script to verify FastMCP installation and basic functionality.
"""

def test_import():
    """Test that FastMCP can be imported."""
    try:
        from fastmcp import FastMCP, Client
        print("✅ FastMCP imports successfully")
        return True
    except ImportError as e:
        print(f"❌ Failed to import FastMCP: {e}")
        return False

def test_server_creation():
    """Test that we can create a basic FastMCP server."""
    try:
        from fastmcp import FastMCP
        
        mcp = FastMCP("Test Server")
        
        @mcp.tool
        def test_tool(message: str) -> str:
            return f"Echo: {message}"
        
        print("✅ Server creation and tool registration successful")
        return True
    except Exception as e:
        print(f"❌ Failed to create server: {e}")
        return False

def test_basic_functionality():
    """Test basic server functionality without running it."""
    try:
        from fastmcp import FastMCP
        
        mcp = FastMCP("Test Server")
        
        @mcp.tool
        def add_numbers(a: int, b: int) -> int:
            """Add two numbers."""
            return a + b
        
        @mcp.resource("test://data")
        def get_test_data() -> dict:
            """Get test data."""
            return {"status": "ok", "data": [1, 2, 3]}
        
        @mcp.prompt
        def test_prompt(name: str) -> str:
            """Test prompt."""
            return f"Hello, {name}!"
        
        print("✅ All component types (tools, resources, prompts) registered successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to register components: {e}")
        return False

def main():
    """Run all tests."""
    print("🧪 Testing FastMCP setup...")
    print("=" * 50)
    
    tests = [
        ("Import test", test_import),
        ("Server creation test", test_server_creation),
        ("Basic functionality test", test_basic_functionality),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        print(f"\n🔍 Running {test_name}...")
        if test_func():
            passed += 1
        else:
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! Your FastMCP setup is ready.")
        print("\n💡 Next steps:")
        print("   1. Run: python hello_world_server.py")
        print("   2. In another terminal, run: python client_example.py")
        print("   3. Or use: fastmcp run hello_world_server.py")
    else:
        print("⚠️  Some tests failed. Please check your FastMCP installation.")
        print("   Try: pip install -r requirements.txt")
    
    return failed == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1) 