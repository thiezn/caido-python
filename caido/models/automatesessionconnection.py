#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, List
from .pageinfo import PageInfo
from .count import Count


class AutomateSessionConnection(BaseModel):
    """Class definition for AutomateSessionConnection."""

    def __init__(
        self, page_info: PageInfo, edges: List, nodes: List, snapshot: str, count: Count
    ):
        """Initialize AutomateSessionConnection class instance."""
        self.page_info = page_info
        self.edges = edges
        self.nodes = nodes
        self.snapshot = snapshot
        self.count = count

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateSessionConnection {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateSessionConnection {self.id}>"
        else:
            return f"<AutomateSessionConnection>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateSessionConnection instance from GraphQL query result."""
        instance = cls(
            page_info=response["pageInfo"],
            edges=response["edges"],
            nodes=response["nodes"],
            snapshot=response["snapshot"],
            count=response["count"],
        )

        return instance
