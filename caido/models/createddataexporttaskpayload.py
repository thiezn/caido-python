#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .dataexporttaskedge import DataExportTaskEdge


class CreatedDataExportTaskPayload(BaseModel):
    """Class definition for CreatedDataExportTaskPayload."""

    def __init__(self, export_task_edge: DataExportTaskEdge):
        """Initialize CreatedDataExportTaskPayload class instance."""
        self.export_task_edge = export_task_edge

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreatedDataExportTaskPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreatedDataExportTaskPayload {self.id}>"
        else:
            return f"<CreatedDataExportTaskPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreatedDataExportTaskPayload instance from GraphQL query result."""
        instance = cls(
            export_task_edge=response["exportTaskEdge"],
        )

        return instance
