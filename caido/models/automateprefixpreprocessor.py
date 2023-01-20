#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class AutomatePrefixPreprocessor(BaseModel):
    """Class definition for AutomatePrefixPreprocessor."""

    def __init__(self, value: str):
        """Initialize AutomatePrefixPreprocessor class instance."""
        self.value = value

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomatePrefixPreprocessor {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomatePrefixPreprocessor {self.id}>"
        else:
            return f"<AutomatePrefixPreprocessor>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomatePrefixPreprocessor instance from GraphQL query result."""
        instance = cls(
            value=response["value"],
        )

        return instance
