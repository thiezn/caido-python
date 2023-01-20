#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .sitemapentry import SitemapEntry


class SitemapEntryEdge(BaseModel):
    """An edge in a connection."""

    def __init__(self, cursor: str, node: SitemapEntry):
        """Initialize SitemapEntryEdge class instance."""
        self.cursor = cursor
        self.node = node

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<SitemapEntryEdge {self.name}>"
        elif hasattr(self, "id"):
            return f"<SitemapEntryEdge {self.id}>"
        else:
            return f"<SitemapEntryEdge>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate SitemapEntryEdge instance from GraphQL query result."""
        instance = cls(
            cursor=response["cursor"],
            node=response["node"],
        )

        return instance
