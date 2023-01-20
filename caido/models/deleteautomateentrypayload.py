#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .deleteautomateentryerror import DeleteAutomateEntryError


class DeleteAutomateEntryPayload(BaseModel):
    """Class definition for DeleteAutomateEntryPayload."""

    def __init__(
        self, deleted_id: Optional[str], user_error: Optional[DeleteAutomateEntryError]
    ):
        """Initialize DeleteAutomateEntryPayload class instance."""
        self.deleted_id = deleted_id
        self.user_error = user_error

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeleteAutomateEntryPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeleteAutomateEntryPayload {self.id}>"
        else:
            return f"<DeleteAutomateEntryPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeleteAutomateEntryPayload instance from GraphQL query result."""
        instance = cls(
            deleted_id=response.get("deletedId"),
            user_error=response.get("userError"),
        )

        return instance
