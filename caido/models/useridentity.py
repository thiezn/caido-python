#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class UserIdentity(BaseModel):
    """Class definition for UserIdentity."""

    def __init__(self, email: str, name: str):
        """Initialize UserIdentity class instance."""
        self.email = email
        self.name = name

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UserIdentity {self.name}>"
        elif hasattr(self, "id"):
            return f"<UserIdentity {self.id}>"
        else:
            return f"<UserIdentity>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UserIdentity instance from GraphQL query result."""
        instance = cls(
            email=response["email"],
            name=response["name"],
        )

        return instance
