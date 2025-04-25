# jira-mcp-server

An MCP server that enables LLMs to interact with Jira through a set of API tools. This server provides a bridge between language models and Jira's functionality, allowing for automated issue management and tracking.

## Features

- Search Jira issues using JQL
- Create new issues
- Get issue details
- Update existing issues
- Delete issues

## Setup in Cursor

Add a new entry to your mcp.json file:
```json
"jira": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "JIRA_BASE_URL",
        "-e",
        "JIRA_EMAIL",
        "-e",
        "JIRA_TOKEN",
        "chasepd/jira-mcp-server:latest"
      ]
      "env":{
        "JIRA_BASE_URL": "[THE BASE URL OF YOUR JIRA INSTANCE]",
        "JIRA_EMAIL": "[EMAIL OF YOUR JIRA ACCOUNT]",
        "JIRA_TOKEN": "[YOUR JIRA API TOKEN]"
      }
    }
```


## Prerequisites

- Python 3.x
- Jira account with API access
- Environment variables for Jira authentication:
  - `JIRA_BASE_URL`
  - `JIRA_EMAIL`
  - `JIRA_TOKEN`

## Dev Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/jira-mcp-server.git
cd jira-mcp-server
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
export JIRA_BASE_URL="your-jira-instance-url"
export JIRA_EMAIL="your-email@example.com"
export JIRA_TOKEN="your-api-token"
```

## Running the Server

### Local Development

```bash
python src/mcp-server.py
```

### Using Docker

The server is available as a Docker image at `chasepd/jira-mcp-server`.

Pull and run the latest version:
```bash
docker pull chasepd/jira-mcp-server:latest
docker run -e JIRA_BASE_URL="your-jira-instance-url" \
           -e JIRA_EMAIL="your-email@example.com" \
           -e JIRA_TOKEN="your-api-token" \
           -p 8000:8000 \
           chasepd/jira-mcp-server:latest
```

## Available Tools

The server provides the following tools for interacting with Jira:

- `jira_search_issues(jql: str)`: Search for issues using JQL
- `jira_create_issue(project_key: str, summary: str, description: str, issuetype: str)`: Create a new issue
- `jira_get_issue(issue_key: str)`: Get details of a specific issue
- `jira_update_issue(issue_key: str, fields: dict)`: Update an existing issue
- `jira_delete_issue(issue_key: str)`: Delete an issue

## Contributing

Contributions are welcome! Please feel free to submit a pull request if there's a new feature you'd like to see.