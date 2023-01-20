#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automateentry import AutomateEntry


class RenameAutomateEntryPayload(BaseModel):
    """Class definition for RenameAutomateEntryPayload."""

    def __init__(self, entry: Optional[AutomateEntry]):
        """Initialize RenameAutomateEntryPayload class instance."""
        self.entry = entry

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<RenameAutomateEntryPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<RenameAutomateEntryPayload {self.id}>"
        else:
            return f"<RenameAutomateEntryPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate RenameAutomateEntryPayload instance from GraphQL query result."""
        instance = cls(
            entry=response.get("entry"),
        )

        return instance
