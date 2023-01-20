#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .dataexportedge import DataExportEdge


class UpdatedDataExportPayload(BaseModel):
    """Class definition for UpdatedDataExportPayload."""

    def __init__(self, data_export_edge: DataExportEdge, snapshot: str):
        """Initialize UpdatedDataExportPayload class instance."""
        self.data_export_edge = data_export_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UpdatedDataExportPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UpdatedDataExportPayload {self.id}>"
        else:
            return f"<UpdatedDataExportPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UpdatedDataExportPayload instance from GraphQL query result."""
        instance = cls(
            data_export_edge=response["dataExportEdge"],
            snapshot=response["snapshot"],
        )

        return instance
