#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class AutomateNullPayload(BaseModel):
    """Class definition for AutomateNullPayload."""

    def __init__(self, quantity: int):
        """Initialize AutomateNullPayload class instance."""
        self.quantity = quantity

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateNullPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateNullPayload {self.id}>"
        else:
            return f"<AutomateNullPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateNullPayload instance from GraphQL query result."""
        instance = cls(
            quantity=response["quantity"],
        )

        return instance
