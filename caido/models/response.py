#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, List
from .alteration import Alteration


class Response(BaseModel):
    """Class definition for Response."""

    def __init__(
        self,
        id: str,
        status_code: int,
        length: int,
        roundtrip_time: int,
        alteration: Alteration,
        edited: bool,
        raw: str,
        edits: List,
    ):
        """Initialize Response class instance."""
        self.id = id
        self.status_code = status_code
        self.length = length
        self.roundtrip_time = roundtrip_time
        self.alteration = alteration
        self.edited = edited
        self.raw = raw
        self.edits = edits

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<Response {self.name}>"
        elif hasattr(self, "id"):
            return f"<Response {self.id}>"
        else:
            return f"<Response>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate Response instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            status_code=response["statusCode"],
            length=response["length"],
            roundtrip_time=response["roundtripTime"],
            alteration=response["alteration"],
            edited=response["edited"],
            raw=response["raw"],
            edits=response["edits"],
        )

        return instance
