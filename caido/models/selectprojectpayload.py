#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .project import Project
from .selectprojectpayloaderror import SelectProjectPayloadError


class SelectProjectPayload(BaseModel):
    """Class definition for SelectProjectPayload."""

    def __init__(
        self, project: Optional[Project], error: Optional[SelectProjectPayloadError]
    ):
        """Initialize SelectProjectPayload class instance."""
        self.project = project
        self.error = error

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<SelectProjectPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<SelectProjectPayload {self.id}>"
        else:
            return f"<SelectProjectPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate SelectProjectPayload instance from GraphQL query result."""
        instance = cls(
            project=response.get("project"),
            error=response.get("error"),
        )

        return instance
