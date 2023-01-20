#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .projectlockederrorreason import ProjectLockedErrorReason


class ProjectLockedUserError(BaseModel):
    """Class definition for ProjectLockedUserError."""

    def __init__(self, reason: ProjectLockedErrorReason, code: str):
        """Initialize ProjectLockedUserError class instance."""
        self.reason = reason
        self.code = code

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<ProjectLockedUserError {self.name}>"
        elif hasattr(self, "id"):
            return f"<ProjectLockedUserError {self.id}>"
        else:
            return f"<ProjectLockedUserError>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate ProjectLockedUserError instance from GraphQL query result."""
        instance = cls(
            reason=response["reason"],
            code=response["code"],
        )

        return instance
