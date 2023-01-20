#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automatetask import AutomateTask
from .pauseautomatetaskerror import PauseAutomateTaskError


class PauseAutomateTaskPayload(BaseModel):
    """Class definition for PauseAutomateTaskPayload."""

    def __init__(
        self,
        automate_task: Optional[AutomateTask],
        user_error: Optional[PauseAutomateTaskError],
    ):
        """Initialize PauseAutomateTaskPayload class instance."""
        self.automate_task = automate_task
        self.user_error = user_error

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<PauseAutomateTaskPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<PauseAutomateTaskPayload {self.id}>"
        else:
            return f"<PauseAutomateTaskPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate PauseAutomateTaskPayload instance from GraphQL query result."""
        instance = cls(
            automate_task=response.get("automateTask"),
            user_error=response.get("userError"),
        )

        return instance
