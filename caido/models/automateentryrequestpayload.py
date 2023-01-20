#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class AutomateEntryRequestPayload(BaseModel):
    """Class definition for AutomateEntryRequestPayload."""

    def __init__(self, raw: Optional[str], position: Optional[int]):
        """Initialize AutomateEntryRequestPayload class instance."""
        self.raw = raw
        self.position = position

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateEntryRequestPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateEntryRequestPayload {self.id}>"
        else:
            return f"<AutomateEntryRequestPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateEntryRequestPayload instance from GraphQL query result."""
        instance = cls(
            raw=response.get("raw"),
            position=response.get("position"),
        )

        return instance
