#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .tamperrule import TamperRule
from .updatetamperruleerror import UpdateTamperRuleError


class UpdateTamperRulePayload(BaseModel):
    """Class definition for UpdateTamperRulePayload."""

    def __init__(
        self, rule: Optional[TamperRule], error: Optional[UpdateTamperRuleError]
    ):
        """Initialize UpdateTamperRulePayload class instance."""
        self.rule = rule
        self.error = error

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UpdateTamperRulePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UpdateTamperRulePayload {self.id}>"
        else:
            return f"<UpdateTamperRulePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UpdateTamperRulePayload instance from GraphQL query result."""
        instance = cls(
            rule=response.get("rule"),
            error=response.get("error"),
        )

        return instance
