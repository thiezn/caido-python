#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeleteReplaySessionCollectionPayload(BaseModel):
    """Class definition for DeleteReplaySessionCollectionPayload."""

    def __init__(self, deleted_id: Optional[str]):
        """Initialize DeleteReplaySessionCollectionPayload class instance."""
        self.deleted_id = deleted_id

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeleteReplaySessionCollectionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeleteReplaySessionCollectionPayload {self.id}>"
        else:
            return f"<DeleteReplaySessionCollectionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeleteReplaySessionCollectionPayload instance from GraphQL query result."""
        instance = cls(
            deleted_id=response.get("deletedId"),
        )

        return instance
