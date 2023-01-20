#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automatesession import AutomateSession


class RenameAutomateSessionPayload(BaseModel):
    """Class definition for RenameAutomateSessionPayload."""

    def __init__(self, session: Optional[AutomateSession]):
        """Initialize RenameAutomateSessionPayload class instance."""
        self.session = session

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<RenameAutomateSessionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<RenameAutomateSessionPayload {self.id}>"
        else:
            return f"<RenameAutomateSessionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate RenameAutomateSessionPayload instance from GraphQL query result."""
        instance = cls(
            session=response.get("session"),
        )

        return instance
