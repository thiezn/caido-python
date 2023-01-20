#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .tamperrulecollection import TamperRuleCollection


class TamperRuleCollectionEdge(BaseModel):
    """An edge in a connection."""

    def __init__(self, cursor: str, node: TamperRuleCollection):
        """Initialize TamperRuleCollectionEdge class instance."""
        self.cursor = cursor
        self.node = node

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<TamperRuleCollectionEdge {self.name}>"
        elif hasattr(self, "id"):
            return f"<TamperRuleCollectionEdge {self.id}>"
        else:
            return f"<TamperRuleCollectionEdge>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate TamperRuleCollectionEdge instance from GraphQL query result."""
        instance = cls(
            cursor=response["cursor"],
            node=response["node"],
        )

        return instance
