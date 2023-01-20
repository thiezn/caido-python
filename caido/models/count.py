#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class Count(BaseModel):
    """Class definition for Count."""

    def __init__(self, value: int, snapshot: str):
        """Initialize Count class instance."""
        self.value = value
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<Count {self.name}>"
        elif hasattr(self, "id"):
            return f"<Count {self.id}>"
        else:
            return f"<Count>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate Count instance from GraphQL query result."""
        instance = cls(
            value=response["value"],
            snapshot=response["snapshot"],
        )

        return instance
