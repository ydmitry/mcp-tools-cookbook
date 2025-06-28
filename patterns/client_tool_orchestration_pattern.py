"""
MCP CLIENT TOOL ORCHESTRATION PATTERN - Sequential web search processing

EXAMPLE: Leveraging native MCP client tools from the server side
This demonstrates how to create MCP server tools that complement and orchestrate
native AI app tools available in the MCP client (like web_search in Cursor).
Server-side tools can extend client-native functionality rather than replace it.

This tool is designed to work in a sequential search workflow:
1. First: Use external web_search to gather initial information
2. Then: Use sequential_web_search to process results and plan next steps
3. Finally: Execute recommended follow-up searches for deeper insights
"""

from fastmcp import FastMCP


def register_client_tool_orchestration_tools(mcp: FastMCP):
    """Register client tool orchestration pattern tools with the MCP server"""
    
    @mcp.tool
    def sequential_web_search(search_results_and_next_search_suggestion: str) -> str:
        """
        A sequential search processing tool that analyzes web search results and processes next search recommendations.

        ⚠️  SEQUENTIAL SEARCH PATTERN: USE ALWAYS AFTER web_search. ALWAYS CALL web_search after this tool as at least one follow-up search is required.

        This tool is designed to be used as part of a sequential search workflow:
        1. 🔍 FIRST: Call external web_search to gather initial information
        2. 📊 THEN: Call this tool to process the results and next search suggestions
        3. 🎯 AFTER: Execute the recommended follow-up searches for deeper insights

        The tool processes search context and prepares for subsequent targeted searches.
        Use this to bridge between initial broad searches and focused follow-up research.

        Args:
            search_results_and_next_search_suggestion: Summary of what was found in previous search
                                                     and suggestions for next search steps

        Returns:
            Processing confirmation (tool primarily works internally)
        """
        # Process the search results internally (simulation of analysis)
        # In a real implementation, this might:
        # - Parse and categorize search results
        # - Identify knowledge gaps
        # - Prepare context for follow-up searches
        # - Log search patterns for optimization

        lines = search_results_and_next_search_suggestion.strip().split('\n')
        total_lines = len(lines)

        return f"✅ Sequential search processing complete. Analyzed {total_lines} lines of search context. Ready for recommended follow-up searches." 