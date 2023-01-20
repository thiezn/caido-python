#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .replaysession import ReplaySession


class ReplaySessionEdge(BaseModel):
    """An edge in a connection."""

    def __init__(self, cursor: str, node: ReplaySession):
        """Initialize ReplaySessionEdge class instance."""
        self.cursor = cursor
        self.node = node

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<ReplaySessionEdge {self.name}>"
        elif hasattr(self, "id"):
            return f"<ReplaySessionEdge {self.id}>"
        else:
            return f"<ReplaySessionEdge>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate ReplaySessionEdge instance from GraphQL query result."""
        instance = cls(
            cursor=response["cursor"],
            node=response["node"],
        )

        return instance
