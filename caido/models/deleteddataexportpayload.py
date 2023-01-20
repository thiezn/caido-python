#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeletedDataExportPayload(BaseModel):
    """Class definition for DeletedDataExportPayload."""

    def __init__(self, deleted_data_export_id: str, snapshot: str):
        """Initialize DeletedDataExportPayload class instance."""
        self.deleted_data_export_id = deleted_data_export_id
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeletedDataExportPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeletedDataExportPayload {self.id}>"
        else:
            return f"<DeletedDataExportPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeletedDataExportPayload instance from GraphQL query result."""
        instance = cls(
            deleted_data_export_id=response["deletedDataExportId"],
            snapshot=response["snapshot"],
        )

        return instance
