#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .tamperrule import TamperRule


class DisableTamperRulePayload(BaseModel):
    """Class definition for DisableTamperRulePayload."""

    def __init__(self, rule: Optional[TamperRule]):
        """Initialize DisableTamperRulePayload class instance."""
        self.rule = rule

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DisableTamperRulePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DisableTamperRulePayload {self.id}>"
        else:
            return f"<DisableTamperRulePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DisableTamperRulePayload instance from GraphQL query result."""
        instance = cls(
            rule=response.get("rule"),
        )

        return instance
