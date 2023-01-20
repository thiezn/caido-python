#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .authenticationtoken import AuthenticationToken
from .createdauthenticationtokenerror import CreatedAuthenticationTokenError


class CreatedAuthenticationTokenPayload(BaseModel):
    """Class definition for CreatedAuthenticationTokenPayload."""

    def __init__(
        self,
        token: Optional[AuthenticationToken],
        error: Optional[CreatedAuthenticationTokenError],
    ):
        """Initialize CreatedAuthenticationTokenPayload class instance."""
        self.token = token
        self.error = error

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreatedAuthenticationTokenPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreatedAuthenticationTokenPayload {self.id}>"
        else:
            return f"<CreatedAuthenticationTokenPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreatedAuthenticationTokenPayload instance from GraphQL query result."""
        instance = cls(
            token=response.get("token"),
            error=response.get("error"),
        )

        return instance
