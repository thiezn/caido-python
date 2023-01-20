#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DropProxyMessagePayload(BaseModel):
    """Class definition for DropProxyMessagePayload."""

    def __init__(self, id: str):
        """Initialize DropProxyMessagePayload class instance."""
        self.id = id

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DropProxyMessagePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DropProxyMessagePayload {self.id}>"
        else:
            return f"<DropProxyMessagePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DropProxyMessagePayload instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
        )

        return instance
