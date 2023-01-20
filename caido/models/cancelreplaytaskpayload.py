#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class CancelReplayTaskPayload(BaseModel):
    """Class definition for CancelReplayTaskPayload."""

    def __init__(self, cancelled_id: str):
        """Initialize CancelReplayTaskPayload class instance."""
        self.cancelled_id = cancelled_id

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CancelReplayTaskPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CancelReplayTaskPayload {self.id}>"
        else:
            return f"<CancelReplayTaskPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CancelReplayTaskPayload instance from GraphQL query result."""
        instance = cls(
            cancelled_id=response["cancelledId"],
        )

        return instance
