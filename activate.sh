#!/bin/bash
# Convenient script to activate the virtual environment
# Usage: source activate.sh

if [ -d "venv" ]; then
    echo "🔌 Activating FastMCP virtual environment..."
    source venv/bin/activate
    echo "✅ Virtual environment activated"
    echo "📋 Available commands:"
    echo "   python mcp_server.py     - Run the server directly"
echo "   fastmcp run mcp_server.py - Run with FastMCP CLI"
    echo "   python simple_test.py            - Run the test suite"
    echo "   python client_example.py         - Interactive client demo"
    echo "   fastmcp inspect mcp_server.py - Inspect the server"
    echo ""
else
    echo "❌ Virtual environment not found!"
    echo "💡 Run: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
fi 