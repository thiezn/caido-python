#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .proxystatus import ProxyStatus


class PauseProxyPayload(BaseModel):
    """Class definition for PauseProxyPayload."""

    def __init__(self, status: ProxyStatus):
        """Initialize PauseProxyPayload class instance."""
        self.status = status

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<PauseProxyPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<PauseProxyPayload {self.id}>"
        else:
            return f"<PauseProxyPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate PauseProxyPayload instance from GraphQL query result."""
        instance = cls(
            status=response["status"],
        )

        return instance
