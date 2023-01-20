#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automatetaskedge import AutomateTaskEdge


class UpdatedAutomateTaskPayload(BaseModel):
    """Class definition for UpdatedAutomateTaskPayload."""

    def __init__(self, automate_task_edge: AutomateTaskEdge, snapshot: str):
        """Initialize UpdatedAutomateTaskPayload class instance."""
        self.automate_task_edge = automate_task_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UpdatedAutomateTaskPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UpdatedAutomateTaskPayload {self.id}>"
        else:
            return f"<UpdatedAutomateTaskPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UpdatedAutomateTaskPayload instance from GraphQL query result."""
        instance = cls(
            automate_task_edge=response["automateTaskEdge"],
            snapshot=response["snapshot"],
        )

        return instance
