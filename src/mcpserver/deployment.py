# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
  """
  Add two numbers and return the result as a string
  Args:
    a: The first number (int)
    b: The second number (int)
  Returns:
    The sum of the two numbers as a string (str)
  """
  return f"The sum of {a} and {b} is {a + b}"