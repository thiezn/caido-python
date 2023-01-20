#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .tamperrule import TamperRule


class TamperRuleEdge(BaseModel):
    """An edge in a connection."""

    def __init__(self, cursor: str, node: TamperRule):
        """Initialize TamperRuleEdge class instance."""
        self.cursor = cursor
        self.node = node

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<TamperRuleEdge {self.name}>"
        elif hasattr(self, "id"):
            return f"<TamperRuleEdge {self.id}>"
        else:
            return f"<TamperRuleEdge>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate TamperRuleEdge instance from GraphQL query result."""
        instance = cls(
            cursor=response["cursor"],
            node=response["node"],
        )

        return instance
