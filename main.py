import logging
from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
from pydantic import BaseModel, Field
from typing import Optional, List
import wikipedia

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("WikipediaMCP")

# Initialize FastMCP
mcp = FastMCP(
    name="Wikipedia MCP Server",
    instructions="Provides tools to query Wikipedia content, including summary, full content, references, categories, images, links, and more."
)

# ------------------------------- Input Schemas -------------------------------

class WikipediaPageInput(BaseModel):
    page: str = Field(..., description="The title of the Wikipedia page to retrieve.")

class WikipediaSearchInput(BaseModel):
    query: str = Field(..., description="Search term to find Wikipedia pages.")

# ------------------------------- Wikipedia Tools -------------------------------

@mcp.tool(name="get_summary", description="Retrieve the summary of a given Wikipedia page.")
def get_summary(input: WikipediaPageInput) -> dict:
    try:
        return {"summary": wikipedia.summary(input.page)}
    except Exception as e:
        raise ToolError(f"Summary error: {str(e)}")

@mcp.tool(name="get_content", description="Retrieve the full plain text content of a Wikipedia page.")
def get_content(input: WikipediaPageInput) -> dict:
    try:
        return {"content": wikipedia.page(input.page).content}
    except Exception as e:
        raise ToolError(f"Content error: {str(e)}")

@mcp.tool(name="get_html", description="Retrieve the rendered HTML of a Wikipedia page.")
def get_html(input: WikipediaPageInput) -> dict:
    try:
        return {"html": wikipedia.page(input.page).html()}
    except Exception as e:
        raise ToolError(f"HTML error: {str(e)}")

@mcp.tool(name="get_images", description="Retrieve a list of image URLs from a Wikipedia page.")
def get_images(input: WikipediaPageInput) -> dict:
    try:
        return {"images": wikipedia.page(input.page).images}
    except Exception as e:
        raise ToolError(f"Images error: {str(e)}")

@mcp.tool(name="get_links", description="Retrieve a list of internal Wikipedia links from a page.")
def get_links(input: WikipediaPageInput) -> dict:
    try:
        return {"links": wikipedia.page(input.page).links}
    except Exception as e:
        raise ToolError(f"Links error: {str(e)}")

@mcp.tool(name="get_references", description="Retrieve external reference URLs cited on a Wikipedia page.")
def get_references(input: WikipediaPageInput) -> dict:
    try:
        return {"references": wikipedia.page(input.page).references}
    except Exception as e:
        raise ToolError(f"References error: {str(e)}")

@mcp.tool(name="get_categories", description="Retrieve the list of categories for a Wikipedia page.")
def get_categories(input: WikipediaPageInput) -> dict:
    try:
        return {"categories": wikipedia.page(input.page).categories}
    except Exception as e:
        raise ToolError(f"Categories error: {str(e)}")

@mcp.tool(name="get_url", description="Retrieve the canonical URL of a Wikipedia page.")
def get_url(input: WikipediaPageInput) -> dict:
    try:
        return {"url": wikipedia.page(input.page).url}
    except Exception as e:
        raise ToolError(f"URL error: {str(e)}")

@mcp.tool(name="get_title", description="Retrieve the title of a Wikipedia page after normalization.")
def get_title(input: WikipediaPageInput) -> dict:
    try:
        return {"title": wikipedia.page(input.page).title}
    except Exception as e:
        raise ToolError(f"Title error: {str(e)}")

@mcp.tool(name="get_page_id", description="Retrieve the internal Wikipedia page ID.")
def get_page_id(input: WikipediaPageInput) -> dict:
    try:
        return {"page_id": wikipedia.page(input.page).pageid}
    except Exception as e:
        raise ToolError(f"Page ID error: {str(e)}")

@mcp.tool(name="search_pages", description="Search Wikipedia for pages matching a query term.")
def search_pages(input: WikipediaSearchInput) -> dict:
    try:
        return {"results": wikipedia.search(input.query)}
    except Exception as e:
        raise ToolError(f"Search error: {str(e)}")

@mcp.tool(name="check_page_exists", description="Check whether a Wikipedia page exists.")
def check_page_exists(input: WikipediaPageInput) -> dict:
    try:
        exists = True
        wikipedia.page(input.page)
    except wikipedia.exceptions.PageError:
        exists = False
    except Exception as e:
        raise ToolError(f"Existence check error: {str(e)}")
    return {"exists": exists}

@mcp.tool(name="disambiguation_options", description="Get disambiguation options for an ambiguous Wikipedia page.")
def disambiguation_options(input: WikipediaPageInput) -> dict:
    try:
        wikipedia.page(input.page)
        return {"disambiguation": False, "options": []}
    except wikipedia.exceptions.DisambiguationError as e:
        return {"disambiguation": True, "options": e.options}
    except Exception as e:
        raise ToolError(f"Disambiguation check error: {str(e)}")

# ------------------------------- Entry Point -------------------------------

if __name__ == "__main__":
    import asyncio
    asyncio.run(mcp.run_async())
