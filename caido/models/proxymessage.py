#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .proxymessagecontent import ProxyMessageContent


class ProxyMessage(BaseModel):
    """Class definition for ProxyMessage."""

    def __init__(self, id: str, content: ProxyMessageContent):
        """Initialize ProxyMessage class instance."""
        self.id = id
        self.content = content

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<ProxyMessage {self.name}>"
        elif hasattr(self, "id"):
            return f"<ProxyMessage {self.id}>"
        else:
            return f"<ProxyMessage>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate ProxyMessage instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            content=response["content"],
        )

        return instance
