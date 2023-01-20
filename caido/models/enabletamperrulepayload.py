#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .tamperrule import TamperRule


class EnableTamperRulePayload(BaseModel):
    """Class definition for EnableTamperRulePayload."""

    def __init__(self, rule: Optional[TamperRule]):
        """Initialize EnableTamperRulePayload class instance."""
        self.rule = rule

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<EnableTamperRulePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<EnableTamperRulePayload {self.id}>"
        else:
            return f"<EnableTamperRulePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate EnableTamperRulePayload instance from GraphQL query result."""
        instance = cls(
            rule=response.get("rule"),
        )

        return instance
