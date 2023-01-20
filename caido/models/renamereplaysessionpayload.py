#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .replaysession import ReplaySession


class RenameReplaySessionPayload(BaseModel):
    """Class definition for RenameReplaySessionPayload."""

    def __init__(self, session: Optional[ReplaySession]):
        """Initialize RenameReplaySessionPayload class instance."""
        self.session = session

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<RenameReplaySessionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<RenameReplaySessionPayload {self.id}>"
        else:
            return f"<RenameReplaySessionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate RenameReplaySessionPayload instance from GraphQL query result."""
        instance = cls(
            session=response.get("session"),
        )

        return instance
