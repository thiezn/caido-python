#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .sitemapentrykind import SitemapEntryKind
from .sitemapentrymetadata import SitemapEntryMetadata
from .requestconnection import RequestConnection


class SitemapEntry(BaseModel):
    """Class definition for SitemapEntry."""

    def __init__(
        self,
        id: str,
        label: str,
        kind: SitemapEntryKind,
        has_descendants: bool,
        requests: RequestConnection,
        parent_id: Optional[str],
        metadata: Optional[SitemapEntryMetadata],
    ):
        """Initialize SitemapEntry class instance."""
        self.id = id
        self.label = label
        self.kind = kind
        self.has_descendants = has_descendants
        self.requests = requests
        self.parent_id = parent_id
        self.metadata = metadata

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<SitemapEntry {self.name}>"
        elif hasattr(self, "id"):
            return f"<SitemapEntry {self.id}>"
        else:
            return f"<SitemapEntry>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate SitemapEntry instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            label=response["label"],
            kind=response["kind"],
            has_descendants=response["hasDescendants"],
            requests=response["requests"],
            parent_id=response.get("parentId"),
            metadata=response.get("metadata"),
        )

        return instance
