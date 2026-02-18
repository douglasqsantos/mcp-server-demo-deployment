# mcp-server-demo-deployment

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that demonstrates packaging and deployment—install from GitHub and use in Cursor, Claude, or any MCP client.

## Features

- **`add`** — Add two integers and return the result (demo tool for testing the server).
- **Install from Git** — Run via `uvx` without cloning; Cursor can start the server from the GitHub URL.
- **Stdio transport** — Works with Cursor, Claude Desktop, and other MCP clients that support stdio.

## Prerequisites

- **Python 3.12+**
- **[uv](https://docs.astral.sh/uv/)** (recommended) or pip

Install uv (macOS/Linux):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Installation

### Option A: Run from GitHub (no clone)

Uses [uvx](https://docs.astral.sh/uv/guides/tools/) to fetch and run the package from the repository:

```bash
uvx --from git+https://github.com/douglasqsantos/mcp-server-demo-deployment.git mcp-server
```

Ensure `uvx` is on your PATH (e.g. `/opt/homebrew/bin/uvx` on macOS with Homebrew).

### Option B: Clone and run locally

```bash
git clone https://github.com/douglasqsantos/mcp-server-demo-deployment.git
cd mcp-server-demo-deployment
uv sync
uv run mcp-server
```

## Add to Cursor

1. **Open the MCP config**
   - **macOS/Linux:** Edit `~/.cursor/mcp.json`
   - **Windows:** Edit `%USERPROFILE%\.cursor\mcp.json`
   - Or in Cursor: **Settings** → **MCP** (if your version supports it).

2. **Add the server**
   Create the file if it doesn’t exist. Use valid JSON:

   ```json
   {
     "mcpServers": {
       "DeploymentDemo": {
         "command": "/opt/homebrew/bin/uvx",
         "args": [
           "--from",
           "git+https://github.com/douglasqsantos/mcp-server-demo-deployment.git",
           "mcp-server"
         ]
       }
     }
   }
   ```

   **Windows:** Use the full path to `uvx` (e.g. `C:\Users\<You>\.local\bin\uvx.exe`) and double backslashes in JSON if needed.

3. **If you already have other servers**
   Add the `"DeploymentDemo"` entry inside the existing `"mcpServers"` object (don’t duplicate the outer braces).

4. **Reload**
   Save the file, then reload Cursor: **Command Palette** (`Ctrl+Shift+P` / `Cmd+Shift+P`) → **Developer: Reload Window**.

5. **Verify**
   In a Cursor chat, confirm that DeploymentDemo (and its tools) appear in the MCP/tools list.

## Usage

- **Standalone (stdio):** `uv run mcp-server` or the `uvx` command above. The server communicates over stdin/stdout.
- **Development:** From the repo, run `mcp dev src/mcpserver/deployment.py` (or the path to your server module) to use the MCP inspector.

## Project structure

```
mcp-server-demo-deployment/
├── src/mcpserver/
│   ├── __main__.py   # Entry point (mcp-server)
│   └── deployment.py # MCP server and tools
├── pyproject.toml
├── README.md
└── LICENSE
```

## Links

- **Source:** [github.com/douglasqsantos/mcp-server-demo-deployment](https://github.com/douglasqsantos/mcp-server-demo-deployment)
- **Bug reports:** [Issues](https://github.com/douglasqsantos/mcp-server-demo-deployment/issues)
- **MCP:** [modelcontextprotocol.io](https://modelcontextprotocol.io)
