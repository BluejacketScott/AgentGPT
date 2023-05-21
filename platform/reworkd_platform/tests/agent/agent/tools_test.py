from reworkd_platform.web.api.agent.tools.reason import Reason
from reworkd_platform.web.api.agent.tools.tools import (
    get_tools_overview,
    get_tool_from_name,
    get_default_tool,
    get_tool_name,
)
from reworkd_platform.web.api.agent.tools.wikipedia_search import Wikipedia


def test_get_tool_name() -> None:
    assert get_tool_name(Wikipedia) == "wikipedia"
    assert get_tool_name(Reason) == "reason"


def test_get_tools_overview() -> None:
    """Simple test to assert that the wikipedia description is what we expect."""
    overview = get_tools_overview()
    wikipedia_description = (
        "Queries Wikipedia for comprehensive insights into specific topics "
        "such as historical entities, corporate bodies, events, "
        "or locations. Argument: Concise, noun-focused query. Less "
        "suitable for real-time queries."
    )

    assert wikipedia_description in overview


def test_get_tool_from_name() -> None:
    assert get_tool_from_name("Wikipedia") == Wikipedia
    assert get_tool_from_name("WiKiPeDia") == Wikipedia
    assert get_tool_from_name("Reason") == Reason
    assert get_tool_from_name("NonExistingTool") == Reason


def test_get_default_tool() -> None:
    assert get_default_tool() == Reason
