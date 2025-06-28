"""
PROMPT EXPOSURE PATTERN - Example of how to share prompts from MCP tools

This demonstrates how MCP tools can expose carefully crafted prompts that users
can copy and use with any AI assistant or human reviewer. Instead of just providing
data or performing actions, MCP becomes a prompt library/repository service.
"""

from fastmcp import FastMCP

def register_prompt_exposure_tools(mcp: FastMCP):
    """Register prompt exposure pattern tools with the MCP server"""
    
    @mcp.tool
    def code_reviewer_prompt() -> str:
        """
        PROMPT EXPOSURE PATTERN: Exposes a comprehensive code review prompt for thorough code analysis.
        
        This tool demonstrates how MCP can serve as a prompt repository, delivering ready-to-use,
        high-quality prompts that can be immediately copy-pasted for various tasks.
        
        Returns a detailed prompt that guides systematic code review covering functionality, 
        performance, security, maintainability, and best practices. Perfect for paste-and-use 
        in code review sessions.
        
        Returns:
            A comprehensive, professional code review prompt
        """
        return """🔍 **COMPREHENSIVE CODE REVIEW PROMPT**

Please conduct a thorough code review of the provided code. Analyze it across the following dimensions:

## 📋 **FUNCTIONALITY & CORRECTNESS**
- Does the code accomplish its intended purpose correctly?
- Are there any logical errors or edge cases not handled?
- Does the implementation match the requirements/specifications?
- Are all input validations and error handling appropriate?

## 🏗️ **CODE STRUCTURE & DESIGN**
- Is the code well-organized and follows clear architectural patterns?
- Are functions/classes appropriately sized and have single responsibilities?
- Is the abstraction level appropriate for the problem domain?
- Are there any design patterns that could improve the structure?

## 📖 **READABILITY & MAINTAINABILITY**
- Is the code easy to read and understand?
- Are variable and function names descriptive and meaningful?
- Is the code properly commented where necessary?
- Would a new developer easily understand this code in 6 months?

## ⚡ **PERFORMANCE & EFFICIENCY**
- Are there any obvious performance bottlenecks?
- Is the algorithmic complexity reasonable for the use case?
- Are resources (memory, network, files) used efficiently?
- Could any operations be optimized without sacrificing readability?

## 🔒 **SECURITY CONSIDERATIONS**
- Are there any potential security vulnerabilities?
- Is input properly sanitized and validated?
- Are sensitive data and credentials handled securely?
- Are there any injection attack vectors?

## 🧪 **TESTING & QUALITY**
- Is the code testable in its current form?
- Are there sufficient unit tests covering main scenarios?
- Are edge cases and error conditions tested?
- Is test coverage adequate for the functionality?

## 🔧 **BEST PRACTICES & CONVENTIONS**
- Does the code follow language-specific best practices?
- Are coding standards and style guidelines followed consistently?
- Is error handling robust and informative?
- Are dependencies and imports organized properly?

## 💡 **SUGGESTIONS FOR IMPROVEMENT**
For each issue identified:
1. **Severity Level**: Critical/Major/Minor/Suggestion
2. **Specific Location**: File and line numbers where applicable
3. **Detailed Explanation**: Why this is an issue
4. **Recommended Solution**: Concrete steps to fix or improve
5. **Alternative Approaches**: Other ways to solve the same problem

## ✅ **POSITIVE FEEDBACK**
- What aspects of the code are well-implemented?
- Which patterns or techniques are particularly good?
- What shows good engineering judgment?

---
**Instructions**: Paste this prompt along with your code for a comprehensive review that covers all critical aspects of code quality.""" 