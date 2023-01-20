#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .replaysession import ReplaySession


class MoveReplaySessionPayload(BaseModel):
    """Class definition for MoveReplaySessionPayload."""

    def __init__(self, session: Optional[ReplaySession]):
        """Initialize MoveReplaySessionPayload class instance."""
        self.session = session

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<MoveReplaySessionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<MoveReplaySessionPayload {self.id}>"
        else:
            return f"<MoveReplaySessionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate MoveReplaySessionPayload instance from GraphQL query result."""
        instance = cls(
            session=response.get("session"),
        )

        return instance
