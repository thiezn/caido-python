#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class SitemapEntryMetadataDomain(BaseModel):
    """Class definition for SitemapEntryMetadataDomain."""

    def __init__(self, is_tls: bool, port: int):
        """Initialize SitemapEntryMetadataDomain class instance."""
        self.is_tls = is_tls
        self.port = port

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<SitemapEntryMetadataDomain {self.name}>"
        elif hasattr(self, "id"):
            return f"<SitemapEntryMetadataDomain {self.id}>"
        else:
            return f"<SitemapEntryMetadataDomain>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate SitemapEntryMetadataDomain instance from GraphQL query result."""
        instance = cls(
            is_tls=response["isTls"],
            port=response["port"],
        )

        return instance
