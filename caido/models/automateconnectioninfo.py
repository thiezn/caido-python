#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class AutomateConnectionInfo(BaseModel):
    """Class definition for AutomateConnectionInfo."""

    def __init__(self, host: str, port: int, is_tls: bool):
        """Initialize AutomateConnectionInfo class instance."""
        self.host = host
        self.port = port
        self.is_tls = is_tls

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateConnectionInfo {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateConnectionInfo {self.id}>"
        else:
            return f"<AutomateConnectionInfo>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateConnectionInfo instance from GraphQL query result."""
        instance = cls(
            host=response["host"],
            port=response["port"],
            is_tls=response["isTls"],
        )

        return instance
