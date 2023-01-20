#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeletedTamperRuleCollectionPayload(BaseModel):
    """Class definition for DeletedTamperRuleCollectionPayload."""

    def __init__(self, deleted_collection_id: str, snapshot: str):
        """Initialize DeletedTamperRuleCollectionPayload class instance."""
        self.deleted_collection_id = deleted_collection_id
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeletedTamperRuleCollectionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeletedTamperRuleCollectionPayload {self.id}>"
        else:
            return f"<DeletedTamperRuleCollectionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeletedTamperRuleCollectionPayload instance from GraphQL query result."""
        instance = cls(
            deleted_collection_id=response["deletedCollectionId"],
            snapshot=response["snapshot"],
        )

        return instance
