#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .authenticationtoken import AuthenticationToken
from .refreshauthenticationtokenerror import RefreshAuthenticationTokenError


class RefreshAuthenticationTokenPayload(BaseModel):
    """Class definition for RefreshAuthenticationTokenPayload."""

    def __init__(
        self,
        token: Optional[AuthenticationToken],
        error: Optional[RefreshAuthenticationTokenError],
    ):
        """Initialize RefreshAuthenticationTokenPayload class instance."""
        self.token = token
        self.error = error

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<RefreshAuthenticationTokenPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<RefreshAuthenticationTokenPayload {self.id}>"
        else:
            return f"<RefreshAuthenticationTokenPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate RefreshAuthenticationTokenPayload instance from GraphQL query result."""
        instance = cls(
            token=response.get("token"),
            error=response.get("error"),
        )

        return instance
