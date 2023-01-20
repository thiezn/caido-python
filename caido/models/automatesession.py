#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, List
from .automatesettings import AutomateSettings
from .automateconnectioninfo import AutomateConnectionInfo


class AutomateSession(BaseModel):
    """Class definition for AutomateSession."""

    def __init__(
        self,
        id: str,
        name: str,
        connection: AutomateConnectionInfo,
        raw: str,
        settings: AutomateSettings,
        created_at: int,
        entries: List,
    ):
        """Initialize AutomateSession class instance."""
        self.id = id
        self.name = name
        self.connection = connection
        self.raw = raw
        self.settings = settings
        self.created_at = created_at
        self.entries = entries

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateSession {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateSession {self.id}>"
        else:
            return f"<AutomateSession>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateSession instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            name=response["name"],
            connection=response["connection"],
            raw=response["raw"],
            settings=response["settings"],
            created_at=response["createdAt"],
            entries=response["entries"],
        )

        return instance
