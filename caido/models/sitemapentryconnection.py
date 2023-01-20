#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, List
from .pageinfo import PageInfo
from .count import Count


class SitemapEntryConnection(BaseModel):
    """Class definition for SitemapEntryConnection."""

    def __init__(
        self, page_info: PageInfo, edges: List, nodes: List, snapshot: str, count: Count
    ):
        """Initialize SitemapEntryConnection class instance."""
        self.page_info = page_info
        self.edges = edges
        self.nodes = nodes
        self.snapshot = snapshot
        self.count = count

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<SitemapEntryConnection {self.name}>"
        elif hasattr(self, "id"):
            return f"<SitemapEntryConnection {self.id}>"
        else:
            return f"<SitemapEntryConnection>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate SitemapEntryConnection instance from GraphQL query result."""
        instance = cls(
            page_info=response["pageInfo"],
            edges=response["edges"],
            nodes=response["nodes"],
            snapshot=response["snapshot"],
            count=response["count"],
        )

        return instance
