#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automatesession import AutomateSession


class UpdateAutomateSessionPayload(BaseModel):
    """Class definition for UpdateAutomateSessionPayload."""

    def __init__(self, session: Optional[AutomateSession]):
        """Initialize UpdateAutomateSessionPayload class instance."""
        self.session = session

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UpdateAutomateSessionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UpdateAutomateSessionPayload {self.id}>"
        else:
            return f"<UpdateAutomateSessionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UpdateAutomateSessionPayload instance from GraphQL query result."""
        instance = cls(
            session=response.get("session"),
        )

        return instance
