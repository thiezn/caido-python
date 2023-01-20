#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeleteAutomateSessionPayload(BaseModel):
    """Class definition for DeleteAutomateSessionPayload."""

    def __init__(self, deleted_id: Optional[str]):
        """Initialize DeleteAutomateSessionPayload class instance."""
        self.deleted_id = deleted_id

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeleteAutomateSessionPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeleteAutomateSessionPayload {self.id}>"
        else:
            return f"<DeleteAutomateSessionPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeleteAutomateSessionPayload instance from GraphQL query result."""
        instance = cls(
            deleted_id=response.get("deletedId"),
        )

        return instance
