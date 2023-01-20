#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .proxymessageconnection import ProxyMessageConnection
from .proxystatus import ProxyStatus


class Proxy(BaseModel):
    """Class definition for Proxy."""

    def __init__(self, status: ProxyStatus, messages: ProxyMessageConnection):
        """Initialize Proxy class instance."""
        self.status = status
        self.messages = messages

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<Proxy {self.name}>"
        elif hasattr(self, "id"):
            return f"<Proxy {self.id}>"
        else:
            return f"<Proxy>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate Proxy instance from GraphQL query result."""
        instance = cls(
            status=response["status"],
            messages=response["messages"],
        )

        return instance
