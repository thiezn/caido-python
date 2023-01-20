#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .scope import Scope


class ScopeEdge(BaseModel):
    """An edge in a connection."""

    def __init__(self, cursor: str, node: Scope):
        """Initialize ScopeEdge class instance."""
        self.cursor = cursor
        self.node = node

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<ScopeEdge {self.name}>"
        elif hasattr(self, "id"):
            return f"<ScopeEdge {self.id}>"
        else:
            return f"<ScopeEdge>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate ScopeEdge instance from GraphQL query result."""
        instance = cls(
            cursor=response["cursor"],
            node=response["node"],
        )

        return instance
