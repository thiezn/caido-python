#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .cancelexporttaskerror import CancelExportTaskError


class CancelDataExportTaskPayload(BaseModel):
    """Class definition for CancelDataExportTaskPayload."""

    def __init__(
        self, cancelled_id: Optional[str], user_error: Optional[CancelExportTaskError]
    ):
        """Initialize CancelDataExportTaskPayload class instance."""
        self.cancelled_id = cancelled_id
        self.user_error = user_error

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CancelDataExportTaskPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CancelDataExportTaskPayload {self.id}>"
        else:
            return f"<CancelDataExportTaskPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CancelDataExportTaskPayload instance from GraphQL query result."""
        instance = cls(
            cancelled_id=response.get("cancelledId"),
            user_error=response.get("userError"),
        )

        return instance
