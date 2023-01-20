#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .deletedataexporterror import DeleteDataExportError


class DeleteDataExportPayload(BaseModel):
    """Class definition for DeleteDataExportPayload."""

    def __init__(
        self, deleted_id: Optional[str], user_error: Optional[DeleteDataExportError]
    ):
        """Initialize DeleteDataExportPayload class instance."""
        self.deleted_id = deleted_id
        self.user_error = user_error

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeleteDataExportPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeleteDataExportPayload {self.id}>"
        else:
            return f"<DeleteDataExportPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeleteDataExportPayload instance from GraphQL query result."""
        instance = cls(
            deleted_id=response.get("deletedId"),
            user_error=response.get("userError"),
        )

        return instance
