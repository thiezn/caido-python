#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automatetaskerrorreason import AutomateTaskErrorReason


class AutomateTaskUserError(BaseModel):
    """Class definition for AutomateTaskUserError."""

    def __init__(self, reason: AutomateTaskErrorReason, code: str):
        """Initialize AutomateTaskUserError class instance."""
        self.reason = reason
        self.code = code

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateTaskUserError {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateTaskUserError {self.id}>"
        else:
            return f"<AutomateTaskUserError>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateTaskUserError instance from GraphQL query result."""
        instance = cls(
            reason=response["reason"],
            code=response["code"],
        )

        return instance
