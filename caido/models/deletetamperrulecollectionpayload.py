#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeleteTamperRuleCollectionPayload(BaseModel):
    """Class definition for DeleteTamperRuleCollectionPayload."""

    def __init__(self, deleted_id: Optional[str]):
        """Initialize DeleteTamperRuleCollectionPayload class instance."""
        self.deleted_id = deleted_id

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeleteTamperRuleCollectionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeleteTamperRuleCollectionPayload {self.id}>"
        else:
            return f"<DeleteTamperRuleCollectionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeleteTamperRuleCollectionPayload instance from GraphQL query result."""
        instance = cls(
            deleted_id=response.get("deletedId"),
        )

        return instance
