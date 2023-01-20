#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automatetask import AutomateTask


class StartAutomateTaskPayload(BaseModel):
    """Class definition for StartAutomateTaskPayload."""

    def __init__(self, automate_task: Optional[AutomateTask]):
        """Initialize StartAutomateTaskPayload class instance."""
        self.automate_task = automate_task

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<StartAutomateTaskPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<StartAutomateTaskPayload {self.id}>"
        else:
            return f"<StartAutomateTaskPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate StartAutomateTaskPayload instance from GraphQL query result."""
        instance = cls(
            automate_task=response.get("automateTask"),
        )

        return instance
