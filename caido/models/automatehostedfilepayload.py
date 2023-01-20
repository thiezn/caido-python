#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class AutomateHostedFilePayload(BaseModel):
    """Class definition for AutomateHostedFilePayload."""

    def __init__(self, id: str, delimiter: Optional[str]):
        """Initialize AutomateHostedFilePayload class instance."""
        self.id = id
        self.delimiter = delimiter

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateHostedFilePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateHostedFilePayload {self.id}>"
        else:
            return f"<AutomateHostedFilePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateHostedFilePayload instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            delimiter=response.get("delimiter"),
        )

        return instance
