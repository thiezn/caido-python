#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .replayentry import ReplayEntry


class ReplayEntryEdge(BaseModel):
    """An edge in a connection."""

    def __init__(self, cursor: str, node: ReplayEntry):
        """Initialize ReplayEntryEdge class instance."""
        self.cursor = cursor
        self.node = node

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<ReplayEntryEdge {self.name}>"
        elif hasattr(self, "id"):
            return f"<ReplayEntryEdge {self.id}>"
        else:
            return f"<ReplayEntryEdge>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate ReplayEntryEdge instance from GraphQL query result."""
        instance = cls(
            cursor=response["cursor"],
            node=response["node"],
        )

        return instance
