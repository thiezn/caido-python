#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .replaytask import ReplayTask


class ReplayTaskEdge(BaseModel):
    """An edge in a connection."""

    def __init__(self, cursor: str, node: ReplayTask):
        """Initialize ReplayTaskEdge class instance."""
        self.cursor = cursor
        self.node = node

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<ReplayTaskEdge {self.name}>"
        elif hasattr(self, "id"):
            return f"<ReplayTaskEdge {self.id}>"
        else:
            return f"<ReplayTaskEdge>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate ReplayTaskEdge instance from GraphQL query result."""
        instance = cls(
            cursor=response["cursor"],
            node=response["node"],
        )

        return instance
