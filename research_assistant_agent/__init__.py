# |---------------------------------------------------------|
# |                                                         |
# |                 Give Feedback / Get Help                |
# | https://github.com/getbindu/Bindu/issues/new/choose    |
# |                                                         |
# |---------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""research-assistant-agent - An Bindu Agent.
"""

from research_assistant_agent.__version__ import __version__
from research_assistant_agent.main import (
    handler,
    initialize_agent,
    main,
)

__all__ = [
    "__version__",
    "handler",
    "initialize_agent",
    "main",
]