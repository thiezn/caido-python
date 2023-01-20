#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class AutomateConcurrencySetting(BaseModel):
    """Class definition for AutomateConcurrencySetting."""

    def __init__(self, workers: int, delay: int):
        """Initialize AutomateConcurrencySetting class instance."""
        self.workers = workers
        self.delay = delay

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateConcurrencySetting {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateConcurrencySetting {self.id}>"
        else:
            return f"<AutomateConcurrencySetting>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateConcurrencySetting instance from GraphQL query result."""
        instance = cls(
            workers=response["workers"],
            delay=response["delay"],
        )

        return instance
