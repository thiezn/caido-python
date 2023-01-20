#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .dataexportedge import DataExportEdge


class CreatedDataExportPayload(BaseModel):
    """Class definition for CreatedDataExportPayload."""

    def __init__(self, data_export_edge: DataExportEdge, snapshot: str):
        """Initialize CreatedDataExportPayload class instance."""
        self.data_export_edge = data_export_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreatedDataExportPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreatedDataExportPayload {self.id}>"
        else:
            return f"<CreatedDataExportPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreatedDataExportPayload instance from GraphQL query result."""
        instance = cls(
            data_export_edge=response["dataExportEdge"],
            snapshot=response["snapshot"],
        )

        return instance
