#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .responsefilter import ResponseFilter
from .requestfilter import RequestFilter


class InterceptEntryFilter(BaseModel):
    """Class definition for InterceptEntryFilter."""

    def __init__(
        self, request: Optional[RequestFilter], response: Optional[ResponseFilter]
    ):
        """Initialize InterceptEntryFilter class instance."""
        self.request = request
        self.response = response

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<InterceptEntryFilter {self.name}>"
        elif hasattr(self, "id"):
            return f"<InterceptEntryFilter {self.id}>"
        else:
            return f"<InterceptEntryFilter>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate InterceptEntryFilter instance from GraphQL query result."""
        instance = cls(
            request=response.get("request"),
            response=response.get("response"),
        )

        return instance
