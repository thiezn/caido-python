#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeletedReplaySessionPayload(BaseModel):
    """Class definition for DeletedReplaySessionPayload."""

    def __init__(self, deleted_session_id: str, snapshot: str):
        """Initialize DeletedReplaySessionPayload class instance."""
        self.deleted_session_id = deleted_session_id
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeletedReplaySessionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeletedReplaySessionPayload {self.id}>"
        else:
            return f"<DeletedReplaySessionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeletedReplaySessionPayload instance from GraphQL query result."""
        instance = cls(
            deleted_session_id=response["deletedSessionId"],
            snapshot=response["snapshot"],
        )

        return instance
