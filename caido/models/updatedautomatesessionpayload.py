#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automatesessionedge import AutomateSessionEdge


class UpdatedAutomateSessionPayload(BaseModel):
    """Class definition for UpdatedAutomateSessionPayload."""

    def __init__(self, automate_session_edge: AutomateSessionEdge, snapshot: str):
        """Initialize UpdatedAutomateSessionPayload class instance."""
        self.automate_session_edge = automate_session_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UpdatedAutomateSessionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UpdatedAutomateSessionPayload {self.id}>"
        else:
            return f"<UpdatedAutomateSessionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UpdatedAutomateSessionPayload instance from GraphQL query result."""
        instance = cls(
            automate_session_edge=response["automateSessionEdge"],
            snapshot=response["snapshot"],
        )

        return instance
