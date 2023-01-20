#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeletedReplaySessionCollectionPayload(BaseModel):
    """Class definition for DeletedReplaySessionCollectionPayload."""

    def __init__(self, deleted_collection_id: str, snapshot: str):
        """Initialize DeletedReplaySessionCollectionPayload class instance."""
        self.deleted_collection_id = deleted_collection_id
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeletedReplaySessionCollectionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeletedReplaySessionCollectionPayload {self.id}>"
        else:
            return f"<DeletedReplaySessionCollectionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeletedReplaySessionCollectionPayload instance from GraphQL query result."""
        instance = cls(
            deleted_collection_id=response["deletedCollectionId"],
            snapshot=response["snapshot"],
        )

        return instance
