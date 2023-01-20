#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class UserEntitlement(BaseModel):
    """Class definition for UserEntitlement."""

    def __init__(self, name: str):
        """Initialize UserEntitlement class instance."""
        self.name = name

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UserEntitlement {self.name}>"
        elif hasattr(self, "id"):
            return f"<UserEntitlement {self.id}>"
        else:
            return f"<UserEntitlement>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UserEntitlement instance from GraphQL query result."""
        instance = cls(
            name=response["name"],
        )

        return instance
