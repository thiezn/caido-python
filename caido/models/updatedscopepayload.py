#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .scopeedge import ScopeEdge


class UpdatedScopePayload(BaseModel):
    """Class definition for UpdatedScopePayload."""

    def __init__(self, scope_edge: ScopeEdge, snapshot: str):
        """Initialize UpdatedScopePayload class instance."""
        self.scope_edge = scope_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UpdatedScopePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UpdatedScopePayload {self.id}>"
        else:
            return f"<UpdatedScopePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UpdatedScopePayload instance from GraphQL query result."""
        instance = cls(
            scope_edge=response["scopeEdge"],
            snapshot=response["snapshot"],
        )

        return instance
