#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automatepreprocessoroptions import AutomatePreprocessorOptions
from .automatepreprocessorkind import AutomatePreprocessorKind


class AutomatePreprocessor(BaseModel):
    """Class definition for AutomatePreprocessor."""

    def __init__(
        self, kind: AutomatePreprocessorKind, options: AutomatePreprocessorOptions
    ):
        """Initialize AutomatePreprocessor class instance."""
        self.kind = kind
        self.options = options

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomatePreprocessor {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomatePreprocessor {self.id}>"
        else:
            return f"<AutomatePreprocessor>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomatePreprocessor instance from GraphQL query result."""
        instance = cls(
            kind=response["kind"],
            options=response["options"],
        )

        return instance
