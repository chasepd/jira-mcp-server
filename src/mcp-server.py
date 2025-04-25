import os

from fastmcp import FastMCP
from jira import JIRA


# Import environment variables
JIRA_URL = os.getenv("JIRA_BASE_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")


mcp = FastMCP(name="Jira MCP Server",
              instructions="""A server that can interact with the Jira API. You can use the following tools to interact with the Jira API:
              - jira_search_issues (jira_search_issues(jql: str) -> list[str]): Search for Jira issues using JQL
              - jira_create_issue (jira_create_issue(project_key: str, summary: str, description: str, issuetype: str) -> str): Create a new Jira issue
              - jira_get_issue (jira_get_issue(issue_key: str) -> dict): Get a Jira issue by its key
              - jira_update_issue (jira_update_issue(issue_key: str, fields: dict) -> None): Update a Jira issue
              - jira_delete_issue (jira_delete_issue(issue_key: str) -> None): Delete a Jira issue
              """)


def initialize_jira():
    return JIRA(
        server=JIRA_URL,
        basic_auth=(JIRA_EMAIL, JIRA_TOKEN)
    )


@mcp.tool()
def jira_search_issues(jql: str):
    """Search for Jira issues using JQL (Jira Query Language)
    
    Args:
        jql (str): The JQL query string to search with
        
    Returns:
        list[str]: List of Jira issue keys matching the query
    """
    jira = initialize_jira()
    issues = jira.search_issues(jql)
    return [issue.key for issue in issues]


@mcp.tool()
def jira_create_issue(project_key: str, summary: str, description: str, issuetype: str):
    """Create a new Jira issue
    
    Args:
        project_key (str): The project key where the issue should be created (e.g. 'PROJ')
        summary (str): The summary/title of the issue
        description (str): The detailed description of the issue
        issuetype (str): The type of issue to create (e.g. 'Bug', 'Task', 'Story')
        
    Returns:
        str: The key of the newly created issue
    """
    jira = initialize_jira()
    issue = jira.create_issue(project=project_key, summary=summary, description=description, issuetype=issuetype)
    return issue.key


@mcp.tool()
def jira_get_issue(issue_key: str):
    """Get a Jira issue by its key
    
    Args:
        issue_key (str): The key of the issue to get
        
    Returns:
        str: A JSON string representation of the Jira issue
    """
    jira = initialize_jira()
    issue = jira.issue(issue_key)
    return issue.raw


@mcp.tool()
def jira_update_issue(issue_key: str, fields: dict):
    """Update a Jira issue
    
    Args:
        issue_key (str): The key of the issue to update
        fields (dict): Dictionary of fields to update and their new values
        
    Returns:
        str: A JSON string representation of the updated Jira issue
    """
    jira = initialize_jira()
    issue = jira.issue(issue_key)
    issue.update(fields=fields)
    return issue.raw


@mcp.tool()
def jira_delete_issue(issue_key: str):
    """Delete a Jira issue
    
    Args:
        issue_key (str): The key of the issue to delete
        
    Returns:
        str: The key of the deleted issue
    """
    jira = initialize_jira()
    issue = jira.issue(issue_key)
    issue.delete()
    return f"Issue {issue_key} deleted"


if __name__ == "__main__":
    mcp.run()

