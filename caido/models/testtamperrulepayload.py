#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .testtamperruleerror import TestTamperRuleError


class TestTamperRulePayload(BaseModel):
    """Class definition for TestTamperRulePayload."""

    def __init__(self, raw: Optional[str], error: Optional[TestTamperRuleError]):
        """Initialize TestTamperRulePayload class instance."""
        self.raw = raw
        self.error = error

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<TestTamperRulePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<TestTamperRulePayload {self.id}>"
        else:
            return f"<TestTamperRulePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate TestTamperRulePayload instance from GraphQL query result."""
        instance = cls(
            raw=response.get("raw"),
            error=response.get("error"),
        )

        return instance
