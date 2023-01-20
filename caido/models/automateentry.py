#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automatesettings import AutomateSettings
from .automatesession import AutomateSession
from .automateconnectioninfo import AutomateConnectionInfo
from .automateentryrequestconnection import AutomateEntryRequestConnection


class AutomateEntry(BaseModel):
    """Class definition for AutomateEntry."""

    def __init__(
        self,
        id: str,
        name: str,
        connection: AutomateConnectionInfo,
        raw: str,
        settings: AutomateSettings,
        created_at: int,
        session: AutomateSession,
        requests: AutomateEntryRequestConnection,
        requests_by_offset: AutomateEntryRequestConnection,
    ):
        """Initialize AutomateEntry class instance."""
        self.id = id
        self.name = name
        self.connection = connection
        self.raw = raw
        self.settings = settings
        self.created_at = created_at
        self.session = session
        self.requests = requests
        self.requests_by_offset = requests_by_offset

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateEntry {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateEntry {self.id}>"
        else:
            return f"<AutomateEntry>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateEntry instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            name=response["name"],
            connection=response["connection"],
            raw=response["raw"],
            settings=response["settings"],
            created_at=response["createdAt"],
            session=response["session"],
            requests=response["requests"],
            requests_by_offset=response["requestsByOffset"],
        )

        return instance
