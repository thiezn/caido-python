#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from datetime import datetime
from .dataexportformat import DataExportFormat
from .dataexportstatus import DataExportStatus


class DataExport(BaseModel):
    """Class definition for DataExport."""

    def __init__(
        self,
        id: str,
        format: DataExportFormat,
        name: str,
        status: DataExportStatus,
        created_at: datetime,
        path: str,
        size: int,
        error: Optional[str],
        download_uri: Optional[str],
    ):
        """Initialize DataExport class instance."""
        self.id = id
        self.format = format
        self.name = name
        self.status = status
        self.created_at = created_at
        self.path = path
        self.size = size
        self.error = error
        self.download_uri = download_uri

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DataExport {self.name}>"
        elif hasattr(self, "id"):
            return f"<DataExport {self.id}>"
        else:
            return f"<DataExport>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DataExport instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            format=response["format"],
            name=response["name"],
            status=response["status"],
            created_at=datetime.strptime(
                response["createdAt"], "%Y-%m-%dT%H:%M:%S.%fz"
            ),
            path=response["path"],
            size=response["size"],
            error=response.get("error"),
            download_uri=response.get("downloadUri"),
        )

        return instance
