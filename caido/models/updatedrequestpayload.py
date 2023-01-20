#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .requestedge import RequestEdge


class UpdatedRequestPayload(BaseModel):
    """Class definition for UpdatedRequestPayload."""

    def __init__(self, request_edge: RequestEdge, snapshot: str):
        """Initialize UpdatedRequestPayload class instance."""
        self.request_edge = request_edge
        self.snapshot = snapshot

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UpdatedRequestPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UpdatedRequestPayload {self.id}>"
        else:
            return f"<UpdatedRequestPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UpdatedRequestPayload instance from GraphQL query result."""
        instance = cls(
            request_edge=response["requestEdge"],
            snapshot=response["snapshot"],
        )

        return instance
