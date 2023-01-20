#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeleteTamperRulePayload(BaseModel):
    """Class definition for DeleteTamperRulePayload."""

    def __init__(self, deleted_id: Optional[str]):
        """Initialize DeleteTamperRulePayload class instance."""
        self.deleted_id = deleted_id

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeleteTamperRulePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeleteTamperRulePayload {self.id}>"
        else:
            return f"<DeleteTamperRulePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeleteTamperRulePayload instance from GraphQL query result."""
        instance = cls(
            deleted_id=response.get("deletedId"),
        )

        return instance
