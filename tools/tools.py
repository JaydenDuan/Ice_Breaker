from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url(name: str):
    """Searches for Linkedin or Twitter Profile Page."""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res[0]["url"]
