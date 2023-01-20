#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .tamperrulecollection import TamperRuleCollection


class RenameTamperRuleCollectionPayload(BaseModel):
    """Class definition for RenameTamperRuleCollectionPayload."""

    def __init__(self, collection: Optional[TamperRuleCollection]):
        """Initialize RenameTamperRuleCollectionPayload class instance."""
        self.collection = collection

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<RenameTamperRuleCollectionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<RenameTamperRuleCollectionPayload {self.id}>"
        else:
            return f"<RenameTamperRuleCollectionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate RenameTamperRuleCollectionPayload instance from GraphQL query result."""
        instance = cls(
            collection=response.get("collection"),
        )

        return instance
