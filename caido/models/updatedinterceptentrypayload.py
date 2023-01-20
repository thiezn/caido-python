#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .interceptentryedge import InterceptEntryEdge


class UpdatedInterceptEntryPayload(BaseModel):
    """Class definition for UpdatedInterceptEntryPayload."""

    def __init__(self, intercept_entry_edge: InterceptEntryEdge, snapshot: str):
        """Initialize UpdatedInterceptEntryPayload class instance."""
        self.intercept_entry_edge = intercept_entry_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UpdatedInterceptEntryPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UpdatedInterceptEntryPayload {self.id}>"
        else:
            return f"<UpdatedInterceptEntryPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UpdatedInterceptEntryPayload instance from GraphQL query result."""
        instance = cls(
            intercept_entry_edge=response["interceptEntryEdge"],
            snapshot=response["snapshot"],
        )

        return instance
