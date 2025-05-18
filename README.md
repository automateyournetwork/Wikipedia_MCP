# Wikipedia MCP Server

This project provides a Model Context Protocol (MCP) server that exposes structured access to Wikipedia content. It uses the [FastMCP](https://github.com/modelcontext/fastmcp) framework to define tools for use in AI workflows, agents, or developer environments like Claude and VS Code.

## ✅ Features

- 🔍 Search for Wikipedia pages
- 📄 Retrieve page summary, full content, and HTML
- 🔗 Extract links, images, references, and categories
- 📌 Detect disambiguation options
- 📌 Check if a page exists
- ⚡ Built on FastMCP — plug into any agent system

---

## 🛠 Installation (Local)

```bash
git clone https://github.com/yourname/wikipedia-mcp-server.git

cd wikipedia-mcp-server

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python wikipedia_mcp_server.py
```

## 🛠 Installation (Docker)

🐳 Docker Setup

Build the container:

```bash
docker build -t wikipedia-mcp .
```

Run the server:

```bash
docker run -it --rm wikipedia-mcp
```

## 🛠 Usage

🧠 Available Tools

| Tool Name          | Description                                      |
|--------------------|--------------------------------------------------|
|--------------------|--------------------------------------------------|
| `get_summary`      | Get a summary of a Wikipedia page                |
| `get_content`      | Get the full content of a Wikipedia page         |
| `get_html`         | Get the rendered HTML of a Wikipedia page        |
| `get_images`       | Get a list of image URLs from a Wikipedia page   |
| `get_links`        | Get a list of internal links from a Wikipedia page|
| `get_references`   | Get a list of external references from a Wikipedia page |
| `get_categories`   | Get a list of Wikipedia categories               |
| `get_url`          | Get the direct Wikipedia URL                     |
| `get_title`        | Get the canonical title of a Wikipedia page      |
| `get_page_id`      | Get the internal Wikipedia page ID               |
| `search_pages`     | Search for Wikipedia page titles                 |
| `check_page_exists`| Check if a Wikipedia page exists                 |
| `disambiguation_options` | Get disambiguation options for ambiguous titles |
|--------------------|--------------------------------------------------|

📁 File Structure

```plaintext
.
├── wikipedia_mcp_server.py
├── requirements.txt
├── Dockerfile
├── README.md

```

💻 VS Code / Claude MCP Integration

Add this to your .vscode/settings.json or Claude configuration to launch this server using MCP:

✅ For Local Python Execution

```json
{
  "mcp": {
    "servers": {
      "wikipedia": {
        "type": "stdio",
        "command": "python3",
        "args": [
          "/absolute/path/to/wikipedia_mcp_server.py"
        ]
      }
    }
  }
}
```

🐳 For Docker Execution

```json
{
  "mcp": {
    "servers": {
      "wikipedia": {
        "type": "stdio",
        "command": "docker",
        "args": [
          "run",
          "--rm",
          "-i",
          "--mount",
          "type=bind,src=${workspaceFolder},dst=/workspace",
          "wikipedia-mcp"
        ]
      }
    }
  }
}
```