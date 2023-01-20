#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automatetaskedge import AutomateTaskEdge


class CreatedAutomateTaskPayload(BaseModel):
    """Class definition for CreatedAutomateTaskPayload."""

    def __init__(self, automate_task_edge: AutomateTaskEdge, snapshot: str):
        """Initialize CreatedAutomateTaskPayload class instance."""
        self.automate_task_edge = automate_task_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreatedAutomateTaskPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreatedAutomateTaskPayload {self.id}>"
        else:
            return f"<CreatedAutomateTaskPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreatedAutomateTaskPayload instance from GraphQL query result."""
        instance = cls(
            automate_task_edge=response["automateTaskEdge"],
            snapshot=response["snapshot"],
        )

        return instance
