#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .authenticationrequest import AuthenticationRequest
from .startauthenticationflowerror import StartAuthenticationFlowError


class StartAuthenticationFlowPayload(BaseModel):
    """Class definition for StartAuthenticationFlowPayload."""

    def __init__(
        self,
        request: Optional[AuthenticationRequest],
        error: Optional[StartAuthenticationFlowError],
    ):
        """Initialize StartAuthenticationFlowPayload class instance."""
        self.request = request
        self.error = error

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<StartAuthenticationFlowPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<StartAuthenticationFlowPayload {self.id}>"
        else:
            return f"<StartAuthenticationFlowPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate StartAuthenticationFlowPayload instance from GraphQL query result."""
        instance = cls(
            request=response.get("request"),
            error=response.get("error"),
        )

        return instance
