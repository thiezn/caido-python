#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .request import Request


class RequestEdge(BaseModel):
    """An edge in a connection."""

    def __init__(self, cursor: str, node: Request):
        """Initialize RequestEdge class instance."""
        self.cursor = cursor
        self.node = node

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<RequestEdge {self.name}>"
        elif hasattr(self, "id"):
            return f"<RequestEdge {self.id}>"
        else:
            return f"<RequestEdge>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate RequestEdge instance from GraphQL query result."""
        instance = cls(
            cursor=response["cursor"],
            node=response["node"],
        )

        return instance
