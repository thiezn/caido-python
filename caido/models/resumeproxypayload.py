#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .proxystatus import ProxyStatus


class ResumeProxyPayload(BaseModel):
    """Class definition for ResumeProxyPayload."""

    def __init__(self, status: ProxyStatus):
        """Initialize ResumeProxyPayload class instance."""
        self.status = status

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<ResumeProxyPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<ResumeProxyPayload {self.id}>"
        else:
            return f"<ResumeProxyPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate ResumeProxyPayload instance from GraphQL query result."""
        instance = cls(
            status=response["status"],
        )

        return instance
