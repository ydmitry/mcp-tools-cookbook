"""
RE-ACT PROMPT EXPOSURE PATTERN - Customizable reasoning-action prompts

This demonstrates how MCP tools can expose dynamic ReAct prompts customized based on
user inputs. This pattern creates personalized reasoning-action prompts by
embedding user-specific parameters (tools, tasks, context) into ReAct templates.

This specific tool generates ReAct (Reasoning + Action) pattern prompts which follow
a reasoning-action pattern with tool calling loop: Think → Act → Observe → Repeat
"""

from fastmcp import FastMCP

def register_react_prompt_exposure_tools(mcp: FastMCP):
    """Register RE-ACT prompt exposure pattern tools with the MCP server"""
    
    @mcp.tool
    def react_prompt_generator(my_available_tools_to_call: str, task: str) -> str:
        """
        PROMPT EXPOSURE PATTERN: Generates a customized ReAct (Reason + Act) pattern prompt.
        
        This tool demonstrates dynamic prompt generation where the prompt template is customized
        based on user inputs. It creates a ReAct prompt that incorporates the specific tools
        the AI can actually call and the task to be accomplished.
        
        Args:
            my_available_tools_to_call: String describing the list of tools that this AI application can actually call (which tools do you have?)
            task: The specific task or goal to be accomplished using the ReAct pattern
        
        Returns:
            A customized ReAct pattern prompt ready to use with any AI assistant
        """
        return f"""🔄 **REACT PATTERN PROMPT**

# System
You're an AI assistant that follows the ReAct (Reason + Act) pattern to perform my personal tasks.
Follow this loop: Thought, Action, Observation.
- Thought: Describe your reasoning about the current state and next steps.
- Action: Specify an action to take to achieve the task.
Add `Finish.` in the end if task is completed.

IMPORTANT! Always return only one thought-action pair per response.

# Available actions (tools)

{my_available_tools_to_call}

# Task

{task}

# Instruction

Please provide your next thought and action.

---
**Usage**: Copy this prompt and start your ReAct session with any AI assistant.""" 