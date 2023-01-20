#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from datetime import datetime


class Project(BaseModel):
    """Class definition for Project."""

    def __init__(
        self,
        id: str,
        name: str,
        version: str,
        updated_at: datetime,
        created_at: datetime,
        path: str,
        size: int,
    ):
        """Initialize Project class instance."""
        self.id = id
        self.name = name
        self.version = version
        self.updated_at = updated_at
        self.created_at = created_at
        self.path = path
        self.size = size

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<Project {self.name}>"
        elif hasattr(self, "id"):
            return f"<Project {self.id}>"
        else:
            return f"<Project>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate Project instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            name=response["name"],
            version=response["version"],
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
