#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .project import Project
from .createprojectpayloaderror import CreateProjectPayloadError


class CreateProjectPayload(BaseModel):
    """Class definition for CreateProjectPayload."""

    def __init__(
        self, project: Optional[Project], error: Optional[CreateProjectPayloadError]
    ):
        """Initialize CreateProjectPayload class instance."""
        self.project = project
        self.error = error

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreateProjectPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreateProjectPayload {self.id}>"
        else:
            return f"<CreateProjectPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreateProjectPayload instance from GraphQL query result."""
        instance = cls(
            project=response.get("project"),
            error=response.get("error"),
        )

        return instance
