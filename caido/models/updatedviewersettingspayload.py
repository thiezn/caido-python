#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .usersettings import UserSettings


class UpdatedViewerSettingsPayload(BaseModel):
    """Class definition for UpdatedViewerSettingsPayload."""

    def __init__(self, settings: UserSettings):
        """Initialize UpdatedViewerSettingsPayload class instance."""
        self.settings = settings

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UpdatedViewerSettingsPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UpdatedViewerSettingsPayload {self.id}>"
        else:
            return f"<UpdatedViewerSettingsPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UpdatedViewerSettingsPayload instance from GraphQL query result."""
        instance = cls(
            settings=response["settings"],
        )

        return instance
