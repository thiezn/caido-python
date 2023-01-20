#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .filter import Filter


class SetFilterPayload(BaseModel):
    """Class definition for SetFilterPayload."""

    def __init__(self, filter: Filter):
        """Initialize SetFilterPayload class instance."""
        self.filter = filter

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<SetFilterPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<SetFilterPayload {self.id}>"
        else:
            return f"<SetFilterPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate SetFilterPayload instance from GraphQL query result."""
        instance = cls(
            filter=response["filter"],
        )

        return instance
