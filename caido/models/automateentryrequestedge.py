#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automateentryrequest import AutomateEntryRequest


class AutomateEntryRequestEdge(BaseModel):
    """An edge in a connection."""

    def __init__(self, cursor: str, node: AutomateEntryRequest):
        """Initialize AutomateEntryRequestEdge class instance."""
        self.cursor = cursor
        self.node = node

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateEntryRequestEdge {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateEntryRequestEdge {self.id}>"
        else:
            return f"<AutomateEntryRequestEdge>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateEntryRequestEdge instance from GraphQL query result."""
        instance = cls(
            cursor=response["cursor"],
            node=response["node"],
        )

        return instance
