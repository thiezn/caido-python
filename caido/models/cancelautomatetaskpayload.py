#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .cancelautomatetaskerror import CancelAutomateTaskError


class CancelAutomateTaskPayload(BaseModel):
    """Class definition for CancelAutomateTaskPayload."""

    def __init__(
        self, cancelled_id: Optional[str], user_error: Optional[CancelAutomateTaskError]
    ):
        """Initialize CancelAutomateTaskPayload class instance."""
        self.cancelled_id = cancelled_id
        self.user_error = user_error

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CancelAutomateTaskPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CancelAutomateTaskPayload {self.id}>"
        else:
            return f"<CancelAutomateTaskPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CancelAutomateTaskPayload instance from GraphQL query result."""
        instance = cls(
            cancelled_id=response.get("cancelledId"),
            user_error=response.get("userError"),
        )

        return instance
