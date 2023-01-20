#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class InvalidRegexUserError(BaseModel):
    """Class definition for InvalidRegexUserError."""

    def __init__(self, term: str, code: str):
        """Initialize InvalidRegexUserError class instance."""
        self.term = term
        self.code = code

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<InvalidRegexUserError {self.name}>"
        elif hasattr(self, "id"):
            return f"<InvalidRegexUserError {self.id}>"
        else:
            return f"<InvalidRegexUserError>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate InvalidRegexUserError instance from GraphQL query result."""
        instance = cls(
            term=response["term"],
            code=response["code"],
        )

        return instance
