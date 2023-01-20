#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .request import Request


class InterceptEntry(BaseModel):
    """Class definition for InterceptEntry."""

    def __init__(self, id: str, request: Request):
        """Initialize InterceptEntry class instance."""
        self.id = id
        self.request = request

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<InterceptEntry {self.name}>"
        elif hasattr(self, "id"):
            return f"<InterceptEntry {self.id}>"
        else:
            return f"<InterceptEntry>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate InterceptEntry instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            request=response["request"],
        )

        return instance
