#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeletedTamperRulePayload(BaseModel):
    """Class definition for DeletedTamperRulePayload."""

    def __init__(self, deleted_rule_id: str, snapshot: str):
        """Initialize DeletedTamperRulePayload class instance."""
        self.deleted_rule_id = deleted_rule_id
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeletedTamperRulePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeletedTamperRulePayload {self.id}>"
        else:
            return f"<DeletedTamperRulePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeletedTamperRulePayload instance from GraphQL query result."""
        instance = cls(
            deleted_rule_id=response["deletedRuleId"],
            snapshot=response["snapshot"],
        )

        return instance
