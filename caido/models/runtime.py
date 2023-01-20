#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .release import Release


class Runtime(BaseModel):
    """Class definition for Runtime."""

    def __init__(
        self, version: str, platform: str, available_update: Optional[Release]
    ):
        """Initialize Runtime class instance."""
        self.version = version
        self.platform = platform
        self.available_update = available_update

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<Runtime {self.name}>"
        elif hasattr(self, "id"):
            return f"<Runtime {self.id}>"
        else:
            return f"<Runtime>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate Runtime instance from GraphQL query result."""
        instance = cls(
            version=response["version"],
            platform=response["platform"],
            available_update=response.get("availableUpdate"),
        )

        return instance
