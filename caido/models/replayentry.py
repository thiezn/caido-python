#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .request import Request


class ReplayEntry(BaseModel):
    """Class definition for ReplayEntry."""

    def __init__(
        self, id: str, session_id: str, request: Request, error: Optional[str]
    ):
        """Initialize ReplayEntry class instance."""
        self.id = id
        self.session_id = session_id
        self.request = request
        self.error = error

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<ReplayEntry {self.name}>"
        elif hasattr(self, "id"):
            return f"<ReplayEntry {self.id}>"
        else:
            return f"<ReplayEntry>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate ReplayEntry instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            session_id=response["sessionId"],
            request=response["request"],
            error=response.get("error"),
        )

        return instance
