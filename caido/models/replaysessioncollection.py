#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, List


class ReplaySessionCollection(BaseModel):
    """Class definition for ReplaySessionCollection."""

    def __init__(self, id: str, name: str, sessions: List):
        """Initialize ReplaySessionCollection class instance."""
        self.id = id
        self.name = name
        self.sessions = sessions

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<ReplaySessionCollection {self.name}>"
        elif hasattr(self, "id"):
            return f"<ReplaySessionCollection {self.id}>"
        else:
            return f"<ReplaySessionCollection>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate ReplaySessionCollection instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            name=response["name"],
            sessions=response["sessions"],
        )

        return instance
