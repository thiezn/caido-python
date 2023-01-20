#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .tamperrule import TamperRule


class MoveTamperRulePayload(BaseModel):
    """Class definition for MoveTamperRulePayload."""

    def __init__(self, rule: Optional[TamperRule]):
        """Initialize MoveTamperRulePayload class instance."""
        self.rule = rule

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<MoveTamperRulePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<MoveTamperRulePayload {self.id}>"
        else:
            return f"<MoveTamperRulePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate MoveTamperRulePayload instance from GraphQL query result."""
        instance = cls(
            rule=response.get("rule"),
        )

        return instance
