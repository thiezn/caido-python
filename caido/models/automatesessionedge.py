#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automatesession import AutomateSession


class AutomateSessionEdge(BaseModel):
    """An edge in a connection."""

    def __init__(self, cursor: str, node: AutomateSession):
        """Initialize AutomateSessionEdge class instance."""
        self.cursor = cursor
        self.node = node

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateSessionEdge {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateSessionEdge {self.id}>"
        else:
            return f"<AutomateSessionEdge>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateSessionEdge instance from GraphQL query result."""
        instance = cls(
            cursor=response["cursor"],
            node=response["node"],
        )

        return instance
