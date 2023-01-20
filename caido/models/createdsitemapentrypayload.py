#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, List
from .sitemapentryedge import SitemapEntryEdge
from .requestedge import RequestEdge


class CreatedSitemapEntryPayload(BaseModel):
    """Class definition for CreatedSitemapEntryPayload."""

    def __init__(
        self,
        sitemap_entry_edge: SitemapEntryEdge,
        ancestor_ids: List,
        snapshot: str,
        request_edge: Optional[RequestEdge],
    ):
        """Initialize CreatedSitemapEntryPayload class instance."""
        self.sitemap_entry_edge = sitemap_entry_edge
        self.ancestor_ids = ancestor_ids
        self.snapshot = snapshot
        self.request_edge = request_edge

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreatedSitemapEntryPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreatedSitemapEntryPayload {self.id}>"
        else:
            return f"<CreatedSitemapEntryPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreatedSitemapEntryPayload instance from GraphQL query result."""
        instance = cls(
            sitemap_entry_edge=response["sitemapEntryEdge"],
            ancestor_ids=response["ancestorIds"],
            snapshot=response["snapshot"],
            request_edge=response.get("requestEdge"),
        )

        return instance
