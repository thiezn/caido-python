#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class UserSubscriptionPlan(BaseModel):
    """Class definition for UserSubscriptionPlan."""

    def __init__(self, name: str):
        """Initialize UserSubscriptionPlan class instance."""
        self.name = name

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UserSubscriptionPlan {self.name}>"
        elif hasattr(self, "id"):
            return f"<UserSubscriptionPlan {self.id}>"
        else:
            return f"<UserSubscriptionPlan>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UserSubscriptionPlan instance from GraphQL query result."""
        instance = cls(
            name=response["name"],
        )

        return instance
