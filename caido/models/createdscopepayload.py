#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .scopeedge import ScopeEdge


class CreatedScopePayload(BaseModel):
    """Class definition for CreatedScopePayload."""

    def __init__(self, scope_edge: ScopeEdge, snapshot: str):
        """Initialize CreatedScopePayload class instance."""
        self.scope_edge = scope_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreatedScopePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreatedScopePayload {self.id}>"
        else:
            return f"<CreatedScopePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreatedScopePayload instance from GraphQL query result."""
        instance = cls(
            scope_edge=response["scopeEdge"],
            snapshot=response["snapshot"],
        )

        return instance
