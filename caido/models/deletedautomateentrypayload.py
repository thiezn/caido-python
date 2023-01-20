#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeletedAutomateEntryPayload(BaseModel):
    """Class definition for DeletedAutomateEntryPayload."""

    def __init__(self, deleted_automate_entry_id: str, snapshot: str):
        """Initialize DeletedAutomateEntryPayload class instance."""
        self.deleted_automate_entry_id = deleted_automate_entry_id
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeletedAutomateEntryPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeletedAutomateEntryPayload {self.id}>"
        else:
            return f"<DeletedAutomateEntryPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeletedAutomateEntryPayload instance from GraphQL query result."""
        instance = cls(
            deleted_automate_entry_id=response["deletedAutomateEntryId"],
            snapshot=response["snapshot"],
        )

        return instance
