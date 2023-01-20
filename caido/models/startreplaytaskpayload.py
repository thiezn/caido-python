#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .replaytask import ReplayTask


class StartReplayTaskPayload(BaseModel):
    """Class definition for StartReplayTaskPayload."""

    def __init__(self, task: ReplayTask):
        """Initialize StartReplayTaskPayload class instance."""
        self.task = task

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<StartReplayTaskPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<StartReplayTaskPayload {self.id}>"
        else:
            return f"<StartReplayTaskPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate StartReplayTaskPayload instance from GraphQL query result."""
        instance = cls(
            task=response["task"],
        )

        return instance
