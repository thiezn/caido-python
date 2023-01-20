#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .interceptentryedge import InterceptEntryEdge


class CreatedInterceptEntryPayload(BaseModel):
    """Class definition for CreatedInterceptEntryPayload."""

    def __init__(self, intercept_entry_edge: InterceptEntryEdge, snapshot: str):
        """Initialize CreatedInterceptEntryPayload class instance."""
        self.intercept_entry_edge = intercept_entry_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreatedInterceptEntryPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreatedInterceptEntryPayload {self.id}>"
        else:
            return f"<CreatedInterceptEntryPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreatedInterceptEntryPayload instance from GraphQL query result."""
        instance = cls(
            intercept_entry_edge=response["interceptEntryEdge"],
            snapshot=response["snapshot"],
        )

        return instance
