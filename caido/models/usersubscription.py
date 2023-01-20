#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, List
from .usersubscriptionplan import UserSubscriptionPlan


class UserSubscription(BaseModel):
    """Class definition for UserSubscription."""

    def __init__(self, plan: UserSubscriptionPlan, entitlements: List):
        """Initialize UserSubscription class instance."""
        self.plan = plan
        self.entitlements = entitlements

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UserSubscription {self.name}>"
        elif hasattr(self, "id"):
            return f"<UserSubscription {self.id}>"
        else:
            return f"<UserSubscription>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UserSubscription instance from GraphQL query result."""
        instance = cls(
            plan=response["plan"],
            entitlements=response["entitlements"],
        )

        return instance
