#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, List
from .request import Request


class AutomateEntryRequest(BaseModel):
    """Class definition for AutomateEntryRequest."""

    def __init__(
        self,
        sequence_id: str,
        automate_entry_id: str,
        payloads: List,
        request: Request,
        error: Optional[str],
    ):
        """Initialize AutomateEntryRequest class instance."""
        self.sequence_id = sequence_id
        self.automate_entry_id = automate_entry_id
        self.payloads = payloads
        self.request = request
        self.error = error

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateEntryRequest {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateEntryRequest {self.id}>"
        else:
            return f"<AutomateEntryRequest>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateEntryRequest instance from GraphQL query result."""
        instance = cls(
            sequence_id=response["sequenceId"],
            automate_entry_id=response["automateEntryId"],
            payloads=response["payloads"],
            request=response["request"],
            error=response.get("error"),
        )

        return instance
