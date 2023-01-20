#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, List


class Scope(BaseModel):
    """Class definition for Scope."""

    def __init__(
        self, id: str, name: str, allowlist: List, denylist: List, indexed: bool
    ):
        """Initialize Scope class instance."""
        self.id = id
        self.name = name
        self.allowlist = allowlist
        self.denylist = denylist
        self.indexed = indexed

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<Scope {self.name}>"
        elif hasattr(self, "id"):
            return f"<Scope {self.id}>"
        else:
            return f"<Scope>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate Scope instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            name=response["name"],
            allowlist=response["allowlist"],
            denylist=response["denylist"],
            indexed=response["indexed"],
        )

        return instance
