#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .replaysessioncollection import ReplaySessionCollection
from .replayentry import ReplayEntry
from .replayentryconnection import ReplayEntryConnection


class ReplaySession(BaseModel):
    """Class definition for ReplaySession."""

    def __init__(
        self,
        id: str,
        name: str,
        entries: ReplayEntryConnection,
        collection: ReplaySessionCollection,
        active_entry: Optional[ReplayEntry],
    ):
        """Initialize ReplaySession class instance."""
        self.id = id
        self.name = name
        self.entries = entries
        self.collection = collection
        self.active_entry = active_entry

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<ReplaySession {self.name}>"
        elif hasattr(self, "id"):
            return f"<ReplaySession {self.id}>"
        else:
            return f"<ReplaySession>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate ReplaySession instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            name=response["name"],
            entries=response["entries"],
            collection=response["collection"],
            active_entry=response.get("activeEntry"),
        )

        return instance
