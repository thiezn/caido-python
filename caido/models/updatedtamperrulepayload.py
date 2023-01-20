#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .tamperruleedge import TamperRuleEdge


class UpdatedTamperRulePayload(BaseModel):
    """Class definition for UpdatedTamperRulePayload."""

    def __init__(self, rule_edge: TamperRuleEdge, snapshot: str):
        """Initialize UpdatedTamperRulePayload class instance."""
        self.rule_edge = rule_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UpdatedTamperRulePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UpdatedTamperRulePayload {self.id}>"
        else:
            return f"<UpdatedTamperRulePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UpdatedTamperRulePayload instance from GraphQL query result."""
        instance = cls(
            rule_edge=response["ruleEdge"],
            snapshot=response["snapshot"],
        )

        return instance
