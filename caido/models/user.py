#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .usersettings import UserSettings
from .userprofile import UserProfile


class User(BaseModel):
    """Class definition for User."""

    def __init__(self, id: str, profile: UserProfile, settings: Optional[UserSettings]):
        """Initialize User class instance."""
        self.id = id
        self.profile = profile
        self.settings = settings

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<User {self.name}>"
        elif hasattr(self, "id"):
            return f"<User {self.id}>"
        else:
            return f"<User>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate User instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            profile=response["profile"],
            settings=response.get("settings"),
        )

        return instance
