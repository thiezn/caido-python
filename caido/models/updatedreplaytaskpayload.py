#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .replaytaskedge import ReplayTaskEdge


class UpdatedReplayTaskPayload(BaseModel):
    """Class definition for UpdatedReplayTaskPayload."""

    def __init__(self, replay_task_edge: ReplayTaskEdge, snapshot: str):
        """Initialize UpdatedReplayTaskPayload class instance."""
        self.replay_task_edge = replay_task_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UpdatedReplayTaskPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UpdatedReplayTaskPayload {self.id}>"
        else:
            return f"<UpdatedReplayTaskPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UpdatedReplayTaskPayload instance from GraphQL query result."""
        instance = cls(
            replay_task_edge=response["replayTaskEdge"],
            snapshot=response["snapshot"],
        )

        return instance
