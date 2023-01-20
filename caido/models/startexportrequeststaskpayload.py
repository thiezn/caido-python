#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .dataexporttask import DataExportTask


class StartExportRequestsTaskPayload(BaseModel):
    """Class definition for StartExportRequestsTaskPayload."""

    def __init__(self, task: Optional[DataExportTask]):
        """Initialize StartExportRequestsTaskPayload class instance."""
        self.task = task

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<StartExportRequestsTaskPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<StartExportRequestsTaskPayload {self.id}>"
        else:
            return f"<StartExportRequestsTaskPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate StartExportRequestsTaskPayload instance from GraphQL query result."""
        instance = cls(
            task=response.get("task"),
        )

        return instance
