#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automatesession import AutomateSession


class DuplicateAutomateSessionPayload(BaseModel):
    """Class definition for DuplicateAutomateSessionPayload."""

    def __init__(self, session: Optional[AutomateSession]):
        """Initialize DuplicateAutomateSessionPayload class instance."""
        self.session = session

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DuplicateAutomateSessionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DuplicateAutomateSessionPayload {self.id}>"
        else:
            return f"<DuplicateAutomateSessionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DuplicateAutomateSessionPayload instance from GraphQL query result."""
        instance = cls(
            session=response.get("session"),
        )

        return instance
