#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, List


class TamperRuleCollection(BaseModel):
    """Class definition for TamperRuleCollection."""

    def __init__(self, id: str, name: str, rules: List):
        """Initialize TamperRuleCollection class instance."""
        self.id = id
        self.name = name
        self.rules = rules

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<TamperRuleCollection {self.name}>"
        elif hasattr(self, "id"):
            return f"<TamperRuleCollection {self.id}>"
        else:
            return f"<TamperRuleCollection>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate TamperRuleCollection instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            name=response["name"],
            rules=response["rules"],
        )

        return instance
