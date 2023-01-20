#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeletedDataExportTaskPayload(BaseModel):
    """Class definition for DeletedDataExportTaskPayload."""

    def __init__(self, deleted_export_task_id: str):
        """Initialize DeletedDataExportTaskPayload class instance."""
        self.deleted_export_task_id = deleted_export_task_id

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeletedDataExportTaskPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeletedDataExportTaskPayload {self.id}>"
        else:
            return f"<DeletedDataExportTaskPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeletedDataExportTaskPayload instance from GraphQL query result."""
        instance = cls(
            deleted_export_task_id=response["deletedExportTaskId"],
        )

        return instance
