#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .dataexporttask import DataExportTask


class DataExportTaskEdge(BaseModel):
    """An edge in a connection."""

    def __init__(self, cursor: str, node: DataExportTask):
        """Initialize DataExportTaskEdge class instance."""
        self.cursor = cursor
        self.node = node

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DataExportTaskEdge {self.name}>"
        elif hasattr(self, "id"):
            return f"<DataExportTaskEdge {self.id}>"
        else:
            return f"<DataExportTaskEdge>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DataExportTaskEdge instance from GraphQL query result."""
        instance = cls(
            cursor=response["cursor"],
            node=response["node"],
        )

        return instance
