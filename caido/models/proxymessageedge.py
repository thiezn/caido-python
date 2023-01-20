#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .proxymessage import ProxyMessage


class ProxyMessageEdge(BaseModel):
    """An edge in a connection."""

    def __init__(self, cursor: str, node: ProxyMessage):
        """Initialize ProxyMessageEdge class instance."""
        self.cursor = cursor
        self.node = node

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<ProxyMessageEdge {self.name}>"
        elif hasattr(self, "id"):
            return f"<ProxyMessageEdge {self.id}>"
        else:
            return f"<ProxyMessageEdge>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate ProxyMessageEdge instance from GraphQL query result."""
        instance = cls(
            cursor=response["cursor"],
            node=response["node"],
        )

        return instance
