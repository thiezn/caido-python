#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class ReleaseLink(BaseModel):
    """Class definition for ReleaseLink."""

    def __init__(self, display: str, platform: str, link: str):
        """Initialize ReleaseLink class instance."""
        self.display = display
        self.platform = platform
        self.link = link

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<ReleaseLink {self.name}>"
        elif hasattr(self, "id"):
            return f"<ReleaseLink {self.id}>"
        else:
            return f"<ReleaseLink>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate ReleaseLink instance from GraphQL query result."""
        instance = cls(
            display=response["display"],
            platform=response["platform"],
            link=response["link"],
        )

        return instance
