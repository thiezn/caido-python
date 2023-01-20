#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .useridentity import UserIdentity
from .usersubscription import UserSubscription


class UserProfile(BaseModel):
    """Class definition for UserProfile."""

    def __init__(self, identity: UserIdentity, subscription: UserSubscription):
        """Initialize UserProfile class instance."""
        self.identity = identity
        self.subscription = subscription

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UserProfile {self.name}>"
        elif hasattr(self, "id"):
            return f"<UserProfile {self.id}>"
        else:
            return f"<UserProfile>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UserProfile instance from GraphQL query result."""
        instance = cls(
            identity=response["identity"],
            subscription=response["subscription"],
        )

        return instance
