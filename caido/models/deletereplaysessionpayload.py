#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeleteReplaySessionPayload(BaseModel):
    """Class definition for DeleteReplaySessionPayload."""

    def __init__(self, deleted_id: Optional[str]):
        """Initialize DeleteReplaySessionPayload class instance."""
        self.deleted_id = deleted_id

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeleteReplaySessionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeleteReplaySessionPayload {self.id}>"
        else:
            return f"<DeleteReplaySessionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeleteReplaySessionPayload instance from GraphQL query result."""
        instance = cls(
            deleted_id=response.get("deletedId"),
        )

        return instance
