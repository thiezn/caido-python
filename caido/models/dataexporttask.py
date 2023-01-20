#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .dataexport import DataExport


class DataExportTask(BaseModel):
    """Class definition for DataExportTask."""

    def __init__(self, id: str, export: DataExport):
        """Initialize DataExportTask class instance."""
        self.id = id
        self.export = export

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DataExportTask {self.name}>"
        elif hasattr(self, "id"):
            return f"<DataExportTask {self.id}>"
        else:
            return f"<DataExportTask>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DataExportTask instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            export=response["export"],
        )

        return instance
