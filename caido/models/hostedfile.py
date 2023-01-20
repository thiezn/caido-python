#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from datetime import datetime


class HostedFile(BaseModel):
    """Class definition for HostedFile."""

    def __init__(
        self,
        id: str,
        name: str,
        updated_at: datetime,
        created_at: datetime,
        path: str,
        size: int,
    ):
        """Initialize HostedFile class instance."""
        self.id = id
        self.name = name
        self.updated_at = updated_at
        self.created_at = created_at
        self.path = path
        self.size = size

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<HostedFile {self.name}>"
        elif hasattr(self, "id"):
            return f"<HostedFile {self.id}>"
        else:
            return f"<HostedFile>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate HostedFile instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            name=response["name"],
            updated_at=datetime.strptime(
                response["updatedAt"], "%Y-%m-%dT%H:%M:%S.%fz"
            ),
            created_at=datetime.strptime(
                response["createdAt"], "%Y-%m-%dT%H:%M:%S.%fz"
            ),
            path=response["path"],
            size=response["size"],
        )

        return instance
