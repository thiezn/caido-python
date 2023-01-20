#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .replayentry import ReplayEntry


class ReplayTask(BaseModel):
    """Class definition for ReplayTask."""

    def __init__(
        self, id: str, error: Optional[str], replay_entry: Optional[ReplayEntry]
    ):
        """Initialize ReplayTask class instance."""
        self.id = id
        self.error = error
        self.replay_entry = replay_entry

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<ReplayTask {self.name}>"
        elif hasattr(self, "id"):
            return f"<ReplayTask {self.id}>"
        else:
            return f"<ReplayTask>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate ReplayTask instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            error=response.get("error"),
            replay_entry=response.get("replayEntry"),
        )

        return instance
