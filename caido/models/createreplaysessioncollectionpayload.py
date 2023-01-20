#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .replaysessioncollection import ReplaySessionCollection


class CreateReplaySessionCollectionPayload(BaseModel):
    """Class definition for CreateReplaySessionCollectionPayload."""

    def __init__(self, collection: Optional[ReplaySessionCollection]):
        """Initialize CreateReplaySessionCollectionPayload class instance."""
        self.collection = collection

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreateReplaySessionCollectionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreateReplaySessionCollectionPayload {self.id}>"
        else:
            return f"<CreateReplaySessionCollectionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreateReplaySessionCollectionPayload instance from GraphQL query result."""
        instance = cls(
            collection=response.get("collection"),
        )

        return instance
