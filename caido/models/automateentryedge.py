#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automateentry import AutomateEntry


class AutomateEntryEdge(BaseModel):
    """An edge in a connection."""

    def __init__(self, cursor: str, node: AutomateEntry):
        """Initialize AutomateEntryEdge class instance."""
        self.cursor = cursor
        self.node = node

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateEntryEdge {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateEntryEdge {self.id}>"
        else:
            return f"<AutomateEntryEdge>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateEntryEdge instance from GraphQL query result."""
        instance = cls(
            cursor=response["cursor"],
            node=response["node"],
        )

        return instance
