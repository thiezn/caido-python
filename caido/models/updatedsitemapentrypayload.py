#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, List
from .sitemapentryedge import SitemapEntryEdge
from .requestedge import RequestEdge


class UpdatedSitemapEntryPayload(BaseModel):
    """Class definition for UpdatedSitemapEntryPayload."""

    def __init__(
        self,
        sitemap_entry_edge: SitemapEntryEdge,
        request_edge: RequestEdge,
        ancestor_ids: List,
        snapshot: str,
    ):
        """Initialize UpdatedSitemapEntryPayload class instance."""
        self.sitemap_entry_edge = sitemap_entry_edge
        self.request_edge = request_edge
        self.ancestor_ids = ancestor_ids
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UpdatedSitemapEntryPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UpdatedSitemapEntryPayload {self.id}>"
        else:
            return f"<UpdatedSitemapEntryPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UpdatedSitemapEntryPayload instance from GraphQL query result."""
        instance = cls(
            sitemap_entry_edge=response["sitemapEntryEdge"],
            request_edge=response["requestEdge"],
            ancestor_ids=response["ancestorIds"],
            snapshot=response["snapshot"],
        )

        return instance
