#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .replaysessioncollection import ReplaySessionCollection


class RenameReplaySessionCollectionPayload(BaseModel):
    """Class definition for RenameReplaySessionCollectionPayload."""

    def __init__(self, collection: Optional[ReplaySessionCollection]):
        """Initialize RenameReplaySessionCollectionPayload class instance."""
        self.collection = collection

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<RenameReplaySessionCollectionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<RenameReplaySessionCollectionPayload {self.id}>"
        else:
            return f"<RenameReplaySessionCollectionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate RenameReplaySessionCollectionPayload instance from GraphQL query result."""
        instance = cls(
            collection=response.get("collection"),
        )

        return instance
