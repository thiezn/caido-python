#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .usersettings import UserSettings


class UpdateViewerSettingsPayload(BaseModel):
    """Class definition for UpdateViewerSettingsPayload."""

    def __init__(self, settings: Optional[UserSettings]):
        """Initialize UpdateViewerSettingsPayload class instance."""
        self.settings = settings

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UpdateViewerSettingsPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UpdateViewerSettingsPayload {self.id}>"
        else:
            return f"<UpdateViewerSettingsPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UpdateViewerSettingsPayload instance from GraphQL query result."""
        instance = cls(
            settings=response.get("settings"),
        )

        return instance
