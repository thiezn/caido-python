#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, List
from datetime import datetime


class AuthenticationToken(BaseModel):
    """Class definition for AuthenticationToken."""

    def __init__(
        self,
        access_token: str,
        expires_at: datetime,
        scopes: List,
        refresh_token: Optional[str],
    ):
        """Initialize AuthenticationToken class instance."""
        self.access_token = access_token
        self.expires_at = expires_at
        self.scopes = scopes
        self.refresh_token = refresh_token

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AuthenticationToken {self.name}>"
        elif hasattr(self, "id"):
            return f"<AuthenticationToken {self.id}>"
        else:
            return f"<AuthenticationToken>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AuthenticationToken instance from GraphQL query result."""
        instance = cls(
            access_token=response["accessToken"],
            expires_at=datetime.strptime(
                response["expiresAt"], "%Y-%m-%dT%H:%M:%S.%fz"
            ),
            scopes=response["scopes"],
            refresh_token=response.get("refreshToken"),
        )

        return instance
