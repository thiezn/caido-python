#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from datetime import datetime


class AuthenticationRequest(BaseModel):
    """Class definition for AuthenticationRequest."""

    def __init__(
        self, id: str, expires_at: datetime, user_code: str, verification_url: str
    ):
        """Initialize AuthenticationRequest class instance."""
        self.id = id
        self.expires_at = expires_at
        self.user_code = user_code
        self.verification_url = verification_url

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AuthenticationRequest {self.name}>"
        elif hasattr(self, "id"):
            return f"<AuthenticationRequest {self.id}>"
        else:
            return f"<AuthenticationRequest>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AuthenticationRequest instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            expires_at=datetime.strptime(
                response["expiresAt"], "%Y-%m-%dT%H:%M:%S.%fz"
            ),
            user_code=response["userCode"],
            verification_url=response["verificationUrl"],
        )

        return instance
