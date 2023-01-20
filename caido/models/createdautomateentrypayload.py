#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automateentryedge import AutomateEntryEdge


class CreatedAutomateEntryPayload(BaseModel):
    """Class definition for CreatedAutomateEntryPayload."""

    def __init__(self, automate_entry_edge: AutomateEntryEdge, snapshot: str):
        """Initialize CreatedAutomateEntryPayload class instance."""
        self.automate_entry_edge = automate_entry_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreatedAutomateEntryPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreatedAutomateEntryPayload {self.id}>"
        else:
            return f"<CreatedAutomateEntryPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreatedAutomateEntryPayload instance from GraphQL query result."""
        instance = cls(
            automate_entry_edge=response["automateEntryEdge"],
            snapshot=response["snapshot"],
        )

        return instance
