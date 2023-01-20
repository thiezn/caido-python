#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class UnknownIdUserError(BaseModel):
    """Class definition for UnknownIdUserError."""

    def __init__(self, id: str, code: str):
        """Initialize UnknownIdUserError class instance."""
        self.id = id
        self.code = code

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UnknownIdUserError {self.name}>"
        elif hasattr(self, "id"):
            return f"<UnknownIdUserError {self.id}>"
        else:
            return f"<UnknownIdUserError>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UnknownIdUserError instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            code=response["code"],
        )

        return instance
