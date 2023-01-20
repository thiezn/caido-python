#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class LogoutPayload(BaseModel):
    """Class definition for LogoutPayload."""

    def __init__(self, success: bool):
        """Initialize LogoutPayload class instance."""
        self.success = success

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<LogoutPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<LogoutPayload {self.id}>"
        else:
            return f"<LogoutPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate LogoutPayload instance from GraphQL query result."""
        instance = cls(
            success=response["success"],
        )

        return instance
