#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .replaysessioncollectionedge import ReplaySessionCollectionEdge


class UpdatedReplaySessionCollectionPayload(BaseModel):
    """Class definition for UpdatedReplaySessionCollectionPayload."""

    def __init__(self, collection_edge: ReplaySessionCollectionEdge, snapshot: str):
        """Initialize UpdatedReplaySessionCollectionPayload class instance."""
        self.collection_edge = collection_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UpdatedReplaySessionCollectionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UpdatedReplaySessionCollectionPayload {self.id}>"
        else:
            return f"<UpdatedReplaySessionCollectionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UpdatedReplaySessionCollectionPayload instance from GraphQL query result."""
        instance = cls(
            collection_edge=response["collectionEdge"],
            snapshot=response["snapshot"],
        )

        return instance
