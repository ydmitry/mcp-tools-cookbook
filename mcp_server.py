#!/usr/bin/env python3
"""
A simple FastMCP server with a hello world tool.

This demonstrates basic FastMCP functionality with:
- Tools: Functions that can be called by LLMs
- MULTI-STEP TOOL PATTERN: Tools that must be called in a specific order
"""

from typing import Dict, Any, Optional
from fastmcp import FastMCP

# Import pattern modules
from patterns.prompt_exposure_tool_pattern import register_prompt_exposure_tools
from patterns.clarification_questions_pattern import register_clarification_questions_tools
from patterns.multi_step_tool_pattern import register_multi_step_tools
from patterns.react_prompt_exposure_pattern import register_react_prompt_exposure_tools
from patterns.client_tool_orchestration_pattern import register_client_tool_orchestration_tools
from patterns.response_driven_tool_navigation_pattern import register_response_driven_navigation_tools

# Initialize the FastMCP server
mcp = FastMCP(
    name="Hello World MCP Server",
    instructions="""
    This is a simple demonstration server that provides a basic greeting functionality.
    Use the hello_world tool to get personalized greetings.

    MULTI-STEP TOOL PATTERN:
    - step1_initialize_workflow MUST be called before step2_execute_workflow
    - The first tool returns an ID that the second tool requires
    """
)

# Register pattern tools
register_prompt_exposure_tools(mcp)
register_clarification_questions_tools(mcp)
register_multi_step_tools(mcp)
register_react_prompt_exposure_tools(mcp)
register_client_tool_orchestration_tools(mcp)
register_response_driven_navigation_tools(mcp)

# =============================================================================
# MAIN - Server execution
# =============================================================================

if __name__ == "__main__":
    print("🚀 Starting Hello World MCP Server...")
    print("📡 Available endpoints:")
    print("   Tools: smart_recipe_generator, sequential_web_search")
    print("   Response-Driven Navigation: tool_with_follow_up, quantum_mood_analyzer, rubber_duck_debugger, coffee_brew_oracle")
    print("   Prompt Exposure: code_reviewer_prompt, react_prompt_generator (ready-to-use prompts)")
    print("   Clarification Pattern: smart_recipe_generator (progressive information gathering)")
    print("   Sequential Pattern: step1_initialize_workflow → step2_execute_workflow")
    print("   Sequential Search: web_search → sequential_web_search → follow-up searches")
    print("\n💡 Run with: fastmcp run mcp_server.py")
    print("   Or directly: python mcp_server.py")
    print()

    # Run the server (default: stdio transport)
    mcp.run()
