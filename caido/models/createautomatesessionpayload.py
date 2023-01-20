#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automatesession import AutomateSession


class CreateAutomateSessionPayload(BaseModel):
    """Class definition for CreateAutomateSessionPayload."""

    def __init__(self, session: Optional[AutomateSession]):
        """Initialize CreateAutomateSessionPayload class instance."""
        self.session = session

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreateAutomateSessionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreateAutomateSessionPayload {self.id}>"
        else:
            return f"<CreateAutomateSessionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreateAutomateSessionPayload instance from GraphQL query result."""
        instance = cls(
            session=response.get("session"),
        )

        return instance
