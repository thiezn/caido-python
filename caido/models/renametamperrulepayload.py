#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .tamperrule import TamperRule


class RenameTamperRulePayload(BaseModel):
    """Class definition for RenameTamperRulePayload."""

    def __init__(self, rule: Optional[TamperRule]):
        """Initialize RenameTamperRulePayload class instance."""
        self.rule = rule

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<RenameTamperRulePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<RenameTamperRulePayload {self.id}>"
        else:
            return f"<RenameTamperRulePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate RenameTamperRulePayload instance from GraphQL query result."""
        instance = cls(
            rule=response.get("rule"),
        )

        return instance
