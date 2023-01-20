#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .tamperrule import TamperRule


class RankTamperRulePayload(BaseModel):
    """Class definition for RankTamperRulePayload."""

    def __init__(self, rule: Optional[TamperRule]):
        """Initialize RankTamperRulePayload class instance."""
        self.rule = rule

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<RankTamperRulePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<RankTamperRulePayload {self.id}>"
        else:
            return f"<RankTamperRulePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate RankTamperRulePayload instance from GraphQL query result."""
        instance = cls(
            rule=response.get("rule"),
        )

        return instance
