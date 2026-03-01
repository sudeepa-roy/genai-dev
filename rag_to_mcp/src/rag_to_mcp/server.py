from importlib import import_module

try:
    from mcp.server.fastmcp import FastMCP as Server
except Exception:
    try:
        Server = getattr(import_module("fastmcp"), "FastMCP")  # type: ignore[assignment]
    except Exception as e:
        raise ImportError("Install 'mcp' (preferred) or 'fastmcp' to run the server") from e


server = Server("rag_to_mcp")


@server.tool()
def ping() -> dict:
    return {"ok": True, "pong": True}


def main() -> None:
    server.run(transport="stdio")


if __name__ == "__main__":
    main()

