#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .deletedautomatetaskerror import DeletedAutomateTaskError


class DeletedAutomateTaskPayload(BaseModel):
    """Class definition for DeletedAutomateTaskPayload."""

    def __init__(
        self,
        deleted_automate_task_id: str,
        snapshot: str,
        error: Optional[DeletedAutomateTaskError],
    ):
        """Initialize DeletedAutomateTaskPayload class instance."""
        self.deleted_automate_task_id = deleted_automate_task_id
        self.snapshot = snapshot
        self.error = error

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeletedAutomateTaskPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeletedAutomateTaskPayload {self.id}>"
        else:
            return f"<DeletedAutomateTaskPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeletedAutomateTaskPayload instance from GraphQL query result."""
        instance = cls(
            deleted_automate_task_id=response["deletedAutomateTaskId"],
            snapshot=response["snapshot"],
            error=response.get("error"),
        )

        return instance
