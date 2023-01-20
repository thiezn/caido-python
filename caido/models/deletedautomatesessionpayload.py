#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeletedAutomateSessionPayload(BaseModel):
    """Class definition for DeletedAutomateSessionPayload."""

    def __init__(self, deleted_automate_session_id: str, snapshot: str):
        """Initialize DeletedAutomateSessionPayload class instance."""
        self.deleted_automate_session_id = deleted_automate_session_id
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeletedAutomateSessionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeletedAutomateSessionPayload {self.id}>"
        else:
            return f"<DeletedAutomateSessionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeletedAutomateSessionPayload instance from GraphQL query result."""
        instance = cls(
            deleted_automate_session_id=response["deletedAutomateSessionId"],
            snapshot=response["snapshot"],
        )

        return instance
