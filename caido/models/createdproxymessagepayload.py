#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .proxymessageedge import ProxyMessageEdge


class CreatedProxyMessagePayload(BaseModel):
    """Class definition for CreatedProxyMessagePayload."""

    def __init__(self, proxy_message_edge: ProxyMessageEdge, snapshot: str):
        """Initialize CreatedProxyMessagePayload class instance."""
        self.proxy_message_edge = proxy_message_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreatedProxyMessagePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreatedProxyMessagePayload {self.id}>"
        else:
            return f"<CreatedProxyMessagePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreatedProxyMessagePayload instance from GraphQL query result."""
        instance = cls(
            proxy_message_edge=response["proxyMessageEdge"],
            snapshot=response["snapshot"],
        )

        return instance
