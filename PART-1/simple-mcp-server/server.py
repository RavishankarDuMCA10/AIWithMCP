from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Simple MCP Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "freindly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "causal": "Please write a causal, relaxed greeting",
    }

    return f"{styles.get(style, styles['formal'])} for someone named {name}"

def main():
    mcp.run()

if __name__ == "__main__":
    main()