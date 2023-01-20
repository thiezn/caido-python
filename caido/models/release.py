#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, List
from datetime import datetime


class Release(BaseModel):
    """Class definition for Release."""

    def __init__(self, version: str, links: List, released_at: datetime):
        """Initialize Release class instance."""
        self.version = version
        self.links = links
        self.released_at = released_at

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<Release {self.name}>"
        elif hasattr(self, "id"):
            return f"<Release {self.id}>"
        else:
            return f"<Release>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate Release instance from GraphQL query result."""
        instance = cls(
            version=response["version"],
            links=response["links"],
            released_at=datetime.strptime(
                response["releasedAt"], "%Y-%m-%dT%H:%M:%S.%fz"
            ),
        )

        return instance
