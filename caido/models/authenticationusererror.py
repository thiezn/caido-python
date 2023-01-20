#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .authenticationerrorreason import AuthenticationErrorReason


class AuthenticationUserError(BaseModel):
    """Class definition for AuthenticationUserError."""

    def __init__(self, reason: AuthenticationErrorReason, code: str):
        """Initialize AuthenticationUserError class instance."""
        self.reason = reason
        self.code = code

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AuthenticationUserError {self.name}>"
        elif hasattr(self, "id"):
            return f"<AuthenticationUserError {self.id}>"
        else:
            return f"<AuthenticationUserError>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AuthenticationUserError instance from GraphQL query result."""
        instance = cls(
            reason=response["reason"],
            code=response["code"],
        )

        return instance
