#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .replaysessionedge import ReplaySessionEdge


class CreatedReplaySessionPayload(BaseModel):
    """Class definition for CreatedReplaySessionPayload."""

    def __init__(self, session_edge: ReplaySessionEdge, snapshot: str):
        """Initialize CreatedReplaySessionPayload class instance."""
        self.session_edge = session_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreatedReplaySessionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreatedReplaySessionPayload {self.id}>"
        else:
            return f"<CreatedReplaySessionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreatedReplaySessionPayload instance from GraphQL query result."""
        instance = cls(
            session_edge=response["sessionEdge"],
            snapshot=response["snapshot"],
        )

        return instance
