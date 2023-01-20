#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeleteProjectPayload(BaseModel):
    """Class definition for DeleteProjectPayload."""

    def __init__(self, deleted_id: Optional[str]):
        """Initialize DeleteProjectPayload class instance."""
        self.deleted_id = deleted_id

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeleteProjectPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeleteProjectPayload {self.id}>"
        else:
            return f"<DeleteProjectPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeleteProjectPayload instance from GraphQL query result."""
        instance = cls(
            deleted_id=response.get("deletedId"),
        )

        return instance
