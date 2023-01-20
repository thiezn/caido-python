#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class NameTakenUserError(BaseModel):
    """Class definition for NameTakenUserError."""

    def __init__(self, name: str, code: str):
        """Initialize NameTakenUserError class instance."""
        self.name = name
        self.code = code

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<NameTakenUserError {self.name}>"
        elif hasattr(self, "id"):
            return f"<NameTakenUserError {self.id}>"
        else:
            return f"<NameTakenUserError>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate NameTakenUserError instance from GraphQL query result."""
        instance = cls(
            name=response["name"],
            code=response["code"],
        )

        return instance
