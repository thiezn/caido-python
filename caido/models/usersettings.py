#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, Any


class UserSettings(BaseModel):
    """Class definition for UserSettings."""

    def __init__(self, migrations: Any, data: Any):
        """Initialize UserSettings class instance."""
        self.migrations = migrations
        self.data = data

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UserSettings {self.name}>"
        elif hasattr(self, "id"):
            return f"<UserSettings {self.id}>"
        else:
            return f"<UserSettings>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UserSettings instance from GraphQL query result."""
        instance = cls(
            migrations=response["migrations"],
            data=response["data"],
        )

        return instance
