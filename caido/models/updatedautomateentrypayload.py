#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automateentryedge import AutomateEntryEdge


class UpdatedAutomateEntryPayload(BaseModel):
    """Class definition for UpdatedAutomateEntryPayload."""

    def __init__(self, automate_entry_edge: AutomateEntryEdge, snapshot: str):
        """Initialize UpdatedAutomateEntryPayload class instance."""
        self.automate_entry_edge = automate_entry_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UpdatedAutomateEntryPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UpdatedAutomateEntryPayload {self.id}>"
        else:
            return f"<UpdatedAutomateEntryPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UpdatedAutomateEntryPayload instance from GraphQL query result."""
        instance = cls(
            automate_entry_edge=response["automateEntryEdge"],
            snapshot=response["snapshot"],
        )

        return instance
