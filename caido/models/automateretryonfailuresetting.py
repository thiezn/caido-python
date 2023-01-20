#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class AutomateRetryOnFailureSetting(BaseModel):
    """Class definition for AutomateRetryOnFailureSetting."""

    def __init__(self, maximum_retries: int, backoff: int):
        """Initialize AutomateRetryOnFailureSetting class instance."""
        self.maximum_retries = maximum_retries
        self.backoff = backoff

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateRetryOnFailureSetting {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateRetryOnFailureSetting {self.id}>"
        else:
            return f"<AutomateRetryOnFailureSetting>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateRetryOnFailureSetting instance from GraphQL query result."""
        instance = cls(
            maximum_retries=response["maximumRetries"],
            backoff=response["backoff"],
        )

        return instance
