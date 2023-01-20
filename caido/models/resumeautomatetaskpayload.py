#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automatetask import AutomateTask
from .resumeautomatetaskerror import ResumeAutomateTaskError


class ResumeAutomateTaskPayload(BaseModel):
    """Class definition for ResumeAutomateTaskPayload."""

    def __init__(
        self,
        automate_task: Optional[AutomateTask],
        user_error: Optional[ResumeAutomateTaskError],
    ):
        """Initialize ResumeAutomateTaskPayload class instance."""
        self.automate_task = automate_task
        self.user_error = user_error

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<ResumeAutomateTaskPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<ResumeAutomateTaskPayload {self.id}>"
        else:
            return f"<ResumeAutomateTaskPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate ResumeAutomateTaskPayload instance from GraphQL query result."""
        instance = cls(
            automate_task=response.get("automateTask"),
            user_error=response.get("userError"),
        )

        return instance
