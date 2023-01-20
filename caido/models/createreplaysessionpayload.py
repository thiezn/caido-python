#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .replaysession import ReplaySession


class CreateReplaySessionPayload(BaseModel):
    """Class definition for CreateReplaySessionPayload."""

    def __init__(self, session: Optional[ReplaySession]):
        """Initialize CreateReplaySessionPayload class instance."""
        self.session = session

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreateReplaySessionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreateReplaySessionPayload {self.id}>"
        else:
            return f"<CreateReplaySessionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreateReplaySessionPayload instance from GraphQL query result."""
        instance = cls(
            session=response.get("session"),
        )

        return instance
