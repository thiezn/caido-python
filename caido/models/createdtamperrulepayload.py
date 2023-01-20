#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .tamperruleedge import TamperRuleEdge


class CreatedTamperRulePayload(BaseModel):
    """Class definition for CreatedTamperRulePayload."""

    def __init__(self, rule_edge: TamperRuleEdge, snapshot: str):
        """Initialize CreatedTamperRulePayload class instance."""
        self.rule_edge = rule_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreatedTamperRulePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreatedTamperRulePayload {self.id}>"
        else:
            return f"<CreatedTamperRulePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreatedTamperRulePayload instance from GraphQL query result."""
        instance = cls(
            rule_edge=response["ruleEdge"],
            snapshot=response["snapshot"],
        )

        return instance
