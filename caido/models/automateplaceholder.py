#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class AutomatePlaceholder(BaseModel):
    """Class definition for AutomatePlaceholder."""

    def __init__(self, start: int, end: int):
        """Initialize AutomatePlaceholder class instance."""
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomatePlaceholder {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomatePlaceholder {self.id}>"
        else:
            return f"<AutomatePlaceholder>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomatePlaceholder instance from GraphQL query result."""
        instance = cls(
            start=response["start"],
            end=response["end"],
        )

        return instance
