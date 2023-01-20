#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class AutomateSuffixPreprocessor(BaseModel):
    """Class definition for AutomateSuffixPreprocessor."""

    def __init__(self, value: str):
        """Initialize AutomateSuffixPreprocessor class instance."""
        self.value = value

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateSuffixPreprocessor {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateSuffixPreprocessor {self.id}>"
        else:
            return f"<AutomateSuffixPreprocessor>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateSuffixPreprocessor instance from GraphQL query result."""
        instance = cls(
            value=response["value"],
        )

        return instance
