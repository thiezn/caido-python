#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeleteScopePayload(BaseModel):
    """Class definition for DeleteScopePayload."""

    def __init__(self, deleted_id: str):
        """Initialize DeleteScopePayload class instance."""
        self.deleted_id = deleted_id

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeleteScopePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeleteScopePayload {self.id}>"
        else:
            return f"<DeleteScopePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeleteScopePayload instance from GraphQL query result."""
        instance = cls(
            deleted_id=response["deletedId"],
        )

        return instance
