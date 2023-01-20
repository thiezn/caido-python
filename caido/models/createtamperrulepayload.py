#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .tamperrule import TamperRule
from .createtamperruleerror import CreateTamperRuleError


class CreateTamperRulePayload(BaseModel):
    """Class definition for CreateTamperRulePayload."""

    def __init__(
        self, rule: Optional[TamperRule], error: Optional[CreateTamperRuleError]
    ):
        """Initialize CreateTamperRulePayload class instance."""
        self.rule = rule
        self.error = error

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreateTamperRulePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreateTamperRulePayload {self.id}>"
        else:
            return f"<CreateTamperRulePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreateTamperRulePayload instance from GraphQL query result."""
        instance = cls(
            rule=response.get("rule"),
            error=response.get("error"),
        )

        return instance
