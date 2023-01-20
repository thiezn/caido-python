#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .tamperstrategy import TamperStrategy
from .tamperrulecollection import TamperRuleCollection


class TamperRule(BaseModel):
    """Class definition for TamperRule."""

    def __init__(
        self,
        id: str,
        name: str,
        strategy: TamperStrategy,
        match_term: str,
        replace_term: str,
        is_regex: bool,
        is_enabled: bool,
        rank: str,
        collection: TamperRuleCollection,
    ):
        """Initialize TamperRule class instance."""
        self.id = id
        self.name = name
        self.strategy = strategy
        self.match_term = match_term
        self.replace_term = replace_term
        self.is_regex = is_regex
        self.is_enabled = is_enabled
        self.rank = rank
        self.collection = collection

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<TamperRule {self.name}>"
        elif hasattr(self, "id"):
            return f"<TamperRule {self.id}>"
        else:
            return f"<TamperRule>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate TamperRule instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            name=response["name"],
            strategy=response["strategy"],
            match_term=response["matchTerm"],
            replace_term=response["replaceTerm"],
            is_regex=response["isRegex"],
            is_enabled=response["isEnabled"],
            rank=response["rank"],
            collection=response["collection"],
        )

        return instance
