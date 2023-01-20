#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class OtherUserError(BaseModel):
    """Class definition for OtherUserError."""

    def __init__(self, code: str):
        """Initialize OtherUserError class instance."""
        self.code = code

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<OtherUserError {self.name}>"
        elif hasattr(self, "id"):
            return f"<OtherUserError {self.id}>"
        else:
            return f"<OtherUserError>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate OtherUserError instance from GraphQL query result."""
        instance = cls(
            code=response["code"],
        )

        return instance
