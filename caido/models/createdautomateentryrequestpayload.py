#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automateentryrequestedge import AutomateEntryRequestEdge


class CreatedAutomateEntryRequestPayload(BaseModel):
    """Class definition for CreatedAutomateEntryRequestPayload."""

    def __init__(
        self, automate_entry_request_edge: AutomateEntryRequestEdge, snapshot: str
    ):
        """Initialize CreatedAutomateEntryRequestPayload class instance."""
        self.automate_entry_request_edge = automate_entry_request_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreatedAutomateEntryRequestPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreatedAutomateEntryRequestPayload {self.id}>"
        else:
            return f"<CreatedAutomateEntryRequestPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreatedAutomateEntryRequestPayload instance from GraphQL query result."""
        instance = cls(
            automate_entry_request_edge=response["automateEntryRequestEdge"],
            snapshot=response["snapshot"],
        )

        return instance
