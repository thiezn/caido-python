#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, List


class AutomateSimpleListPayload(BaseModel):
    """Class definition for AutomateSimpleListPayload."""

    def __init__(self, list: List):
        """Initialize AutomateSimpleListPayload class instance."""
        self.list = list

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateSimpleListPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateSimpleListPayload {self.id}>"
        else:
            return f"<AutomateSimpleListPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateSimpleListPayload instance from GraphQL query result."""
        instance = cls(
            list=response["list"],
        )

        return instance
