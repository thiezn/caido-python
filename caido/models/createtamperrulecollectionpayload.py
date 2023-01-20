#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .tamperrulecollection import TamperRuleCollection


class CreateTamperRuleCollectionPayload(BaseModel):
    """Class definition for CreateTamperRuleCollectionPayload."""

    def __init__(self, collection: Optional[TamperRuleCollection]):
        """Initialize CreateTamperRuleCollectionPayload class instance."""
        self.collection = collection

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreateTamperRuleCollectionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreateTamperRuleCollectionPayload {self.id}>"
        else:
            return f"<CreateTamperRuleCollectionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreateTamperRuleCollectionPayload instance from GraphQL query result."""
        instance = cls(
            collection=response.get("collection"),
        )

        return instance
