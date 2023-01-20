#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .replaysessioncollectionedge import ReplaySessionCollectionEdge


class CreatedReplaySessionCollectionPayload(BaseModel):
    """Class definition for CreatedReplaySessionCollectionPayload."""

    def __init__(self, collection_edge: ReplaySessionCollectionEdge, snapshot: str):
        """Initialize CreatedReplaySessionCollectionPayload class instance."""
        self.collection_edge = collection_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreatedReplaySessionCollectionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreatedReplaySessionCollectionPayload {self.id}>"
        else:
            return f"<CreatedReplaySessionCollectionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreatedReplaySessionCollectionPayload instance from GraphQL query result."""
        instance = cls(
            collection_edge=response["collectionEdge"],
            snapshot=response["snapshot"],
        )

        return instance
