"""
MULTI-STEP TOOL PATTERN - Tools that must be called in specific order

This pattern demonstrates how to create interdependent tools where:
1. step1_initialize_workflow creates state and returns an identifier
2. step2_execute_workflow requires that identifier to function
3. Calling step2 without step1 will result in an error

This is useful for workflows, authentication flows, data pipelines, etc.
"""

import uuid
from typing import Dict, Any, Optional
from fastmcp import FastMCP

# =============================================================================
# WORKFLOW STORAGE - In-memory storage for workflow management
# =============================================================================

# Simple in-memory storage for workflows
_workflows: Dict[str, Dict[str, Any]] = {}


def register_multi_step_tools(mcp: FastMCP):
    """Register multi-step tool pattern tools with the MCP server"""
    
    @mcp.tool
    def step1_initialize_workflow(workflow_name: str, description: str = "", parameters: Optional[Dict[str, Any]] = None) -> str:
        """
        STEP 1: Initialize a new workflow with the given name and parameters.
        
        ⚠️  MULTI-STEP TOOL PATTERN: This tool MUST be called before step2_execute_workflow
        
        This tool sets up the workflow configuration and returns a unique workflow ID 
        that is required by step2_execute_workflow. The second tool will fail if this 
        tool hasn't been called first.
        
        Args:
            workflow_name: Name of the workflow to initialize
            description: Optional description of what this workflow does
            parameters: Optional dictionary of parameters for the workflow
        
        Returns:
            A workflow ID that MUST be used with step2_execute_workflow
        """
        if parameters is None:
            parameters = {}
        
        # Generate a unique workflow ID
        workflow_id = str(uuid.uuid4())
        
        # Store the workflow configuration
        _workflows[workflow_id] = {
            "name": workflow_name,
            "description": description,
            "parameters": parameters,
            "status": "initialized",
            "created_at": "now"  # In a real implementation, you'd use datetime
        }
        
        return f"✅ STEP 1 COMPLETE: Workflow '{workflow_name}' initialized successfully!\n🆔 Workflow ID: {workflow_id}\n📝 Description: {description or 'No description provided'}\n⚙️ Parameters: {len(parameters)} configured\n\n🔄 NEXT STEP: Call step2_execute_workflow with this workflow ID to execute the workflow."

    @mcp.tool
    def step2_execute_workflow(workflow_id: str) -> str:
        """
        STEP 2: Execute a previously initialized workflow.
        
        ⚠️  MULTI-STEP TOOL PATTERN: This tool requires step1_initialize_workflow to be called first
        
        This tool will ONLY work if step1_initialize_workflow has been called first to create 
        the workflow. It looks up the workflow configuration using the provided ID and executes 
        the workflow steps. If the workflow ID doesn't exist, this tool will return an error.
        
        Args:
            workflow_id: The workflow ID returned by step1_initialize_workflow (REQUIRED)
        
        Returns:
            The result of executing the workflow, or an error if step1 wasn't called first
        """
        # Check if workflow exists (enforcing sequential pattern)
        if workflow_id not in _workflows:
            return f"❌ SEQUENTIAL PATTERN ERROR: Workflow ID '{workflow_id}' not found!\n\n💡 You must call step1_initialize_workflow FIRST to create a workflow before calling this tool.\n🔄 Correct order: step1_initialize_workflow → step2_execute_workflow"
        
        workflow = _workflows[workflow_id]
        
        # Check if workflow is in the right state
        if workflow["status"] != "initialized":
            return f"❌ Error: Workflow '{workflow['name']}' is in '{workflow['status']}' state, not ready for execution."
        
        # Update status to executing
        workflow["status"] = "executing"
        
        # Simulate workflow execution (in a real implementation, this would do actual work)
        workflow_name = workflow["name"]
        parameters = workflow["parameters"]
        description = workflow["description"]
        
        # Simple execution simulation based on workflow name
        if "test" in workflow_name.lower():
            result = f"🧪 Test workflow executed successfully!\n✅ All tests passed\n📊 Test coverage: 95%"
        elif "deploy" in workflow_name.lower():
            result = f"🚀 Deployment workflow executed successfully!\n✅ Application deployed to production\n🌐 Service is now live"
        elif "backup" in workflow_name.lower():
            result = f"💾 Backup workflow executed successfully!\n✅ Data backup completed\n📦 Backup size: 2.3GB"
        else:
            result = f"⚙️ Custom workflow executed successfully!\n✅ All workflow steps completed\n🎯 Workflow goals achieved"
        
        # Update status to completed
        workflow["status"] = "completed"
        
        return f"🎉 STEP 2 COMPLETE: Workflow '{workflow_name}' executed successfully!\n\n{result}\n\n📋 Workflow Details:\n🆔 ID: {workflow_id}\n📝 Description: {description or 'No description'}\n⚙️ Parameters used: {len(parameters)}\n✅ Status: {workflow['status']}\n\n✅ SEQUENTIAL PATTERN SUCCESS: Both steps completed in correct order!" 