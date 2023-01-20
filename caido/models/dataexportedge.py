#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .dataexport import DataExport


class DataExportEdge(BaseModel):
    """An edge in a connection."""

    def __init__(self, cursor: str, node: DataExport):
        """Initialize DataExportEdge class instance."""
        self.cursor = cursor
        self.node = node

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DataExportEdge {self.name}>"
        elif hasattr(self, "id"):
            return f"<DataExportEdge {self.id}>"
        else:
            return f"<DataExportEdge>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DataExportEdge instance from GraphQL query result."""
        instance = cls(
            cursor=response["cursor"],
            node=response["node"],
        )

        return instance
