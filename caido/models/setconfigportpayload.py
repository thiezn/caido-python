#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .globalconfig import GlobalConfig


class SetConfigPortPayload(BaseModel):
    """Class definition for SetConfigPortPayload."""

    def __init__(self, config: GlobalConfig):
        """Initialize SetConfigPortPayload class instance."""
        self.config = config

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<SetConfigPortPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<SetConfigPortPayload {self.id}>"
        else:
            return f"<SetConfigPortPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate SetConfigPortPayload instance from GraphQL query result."""
        instance = cls(
            config=response["config"],
        )

        return instance
