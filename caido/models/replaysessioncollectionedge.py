#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .replaysessioncollection import ReplaySessionCollection


class ReplaySessionCollectionEdge(BaseModel):
    """An edge in a connection."""

    def __init__(self, cursor: str, node: ReplaySessionCollection):
        """Initialize ReplaySessionCollectionEdge class instance."""
        self.cursor = cursor
        self.node = node

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<ReplaySessionCollectionEdge {self.name}>"
        elif hasattr(self, "id"):
            return f"<ReplaySessionCollectionEdge {self.id}>"
        else:
            return f"<ReplaySessionCollectionEdge>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate ReplaySessionCollectionEdge instance from GraphQL query result."""
        instance = cls(
            cursor=response["cursor"],
            node=response["node"],
        )

        return instance
