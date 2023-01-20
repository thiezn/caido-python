#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .tamperrulecollectionedge import TamperRuleCollectionEdge


class CreatedTamperRuleCollectionPayload(BaseModel):
    """Class definition for CreatedTamperRuleCollectionPayload."""

    def __init__(self, collection_edge: TamperRuleCollectionEdge, snapshot: str):
        """Initialize CreatedTamperRuleCollectionPayload class instance."""
        self.collection_edge = collection_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreatedTamperRuleCollectionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreatedTamperRuleCollectionPayload {self.id}>"
        else:
            return f"<CreatedTamperRuleCollectionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreatedTamperRuleCollectionPayload instance from GraphQL query result."""
        instance = cls(
            collection_edge=response["collectionEdge"],
            snapshot=response["snapshot"],
        )

        return instance
