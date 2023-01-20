#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .requestedge import RequestEdge


class CreatedRequestPayload(BaseModel):
    """Class definition for CreatedRequestPayload."""

    def __init__(self, request_edge: RequestEdge, snapshot: str):
        """Initialize CreatedRequestPayload class instance."""
        self.request_edge = request_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreatedRequestPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreatedRequestPayload {self.id}>"
        else:
            return f"<CreatedRequestPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreatedRequestPayload instance from GraphQL query result."""
        instance = cls(
            request_edge=response["requestEdge"],
            snapshot=response["snapshot"],
        )

        return instance
