#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .dataexport import DataExport


class RenameDataExportPayload(BaseModel):
    """Class definition for RenameDataExportPayload."""

    def __init__(self, export: Optional[DataExport]):
        """Initialize RenameDataExportPayload class instance."""
        self.export = export

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<RenameDataExportPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<RenameDataExportPayload {self.id}>"
        else:
            return f"<RenameDataExportPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate RenameDataExportPayload instance from GraphQL query result."""
        instance = cls(
            export=response.get("export"),
        )

        return instance
