#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class ForwardProxyMessagePayload(BaseModel):
    """Class definition for ForwardProxyMessagePayload."""

    def __init__(self, id: str):
        """Initialize ForwardProxyMessagePayload class instance."""
        self.id = id

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<ForwardProxyMessagePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<ForwardProxyMessagePayload {self.id}>"
        else:
            return f"<ForwardProxyMessagePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate ForwardProxyMessagePayload instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
        )

        return instance
