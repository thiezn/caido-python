#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .replaysession import ReplaySession


class SetActiveReplaySessionEntryPayload(BaseModel):
    """Class definition for SetActiveReplaySessionEntryPayload."""

    def __init__(self, session: Optional[ReplaySession]):
        """Initialize SetActiveReplaySessionEntryPayload class instance."""
        self.session = session

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<SetActiveReplaySessionEntryPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<SetActiveReplaySessionEntryPayload {self.id}>"
        else:
            return f"<SetActiveReplaySessionEntryPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate SetActiveReplaySessionEntryPayload instance from GraphQL query result."""
        instance = cls(
            session=response.get("session"),
        )

        return instance
