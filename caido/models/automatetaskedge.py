#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automatetask import AutomateTask


class AutomateTaskEdge(BaseModel):
    """An edge in a connection."""

    def __init__(self, cursor: str, node: AutomateTask):
        """Initialize AutomateTaskEdge class instance."""
        self.cursor = cursor
        self.node = node

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateTaskEdge {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateTaskEdge {self.id}>"
        else:
            return f"<AutomateTaskEdge>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateTaskEdge instance from GraphQL query result."""
        instance = cls(
            cursor=response["cursor"],
            node=response["node"],
        )

        return instance
