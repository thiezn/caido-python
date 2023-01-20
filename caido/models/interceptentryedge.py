#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .interceptentry import InterceptEntry


class InterceptEntryEdge(BaseModel):
    """An edge in a connection."""

    def __init__(self, cursor: str, node: InterceptEntry):
        """Initialize InterceptEntryEdge class instance."""
        self.cursor = cursor
        self.node = node

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<InterceptEntryEdge {self.name}>"
        elif hasattr(self, "id"):
            return f"<InterceptEntryEdge {self.id}>"
        else:
            return f"<InterceptEntryEdge>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate InterceptEntryEdge instance from GraphQL query result."""
        instance = cls(
            cursor=response["cursor"],
            node=response["node"],
        )

        return instance
