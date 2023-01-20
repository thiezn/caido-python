#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeletedScopePayload(BaseModel):
    """Class definition for DeletedScopePayload."""

    def __init__(self, deleted_scope_id: str, snapshot: str):
        """Initialize DeletedScopePayload class instance."""
        self.deleted_scope_id = deleted_scope_id
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeletedScopePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeletedScopePayload {self.id}>"
        else:
            return f"<DeletedScopePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeletedScopePayload instance from GraphQL query result."""
        instance = cls(
            deleted_scope_id=response["deletedScopeId"],
            snapshot=response["snapshot"],
        )

        return instance
