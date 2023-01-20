#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .requestfilter import RequestFilter
from .responsefilter import ResponseFilter
from .stringfilter import StringFilter


class RequestResponseFilter(BaseModel):
    """Class definition for RequestResponseFilter."""

    def __init__(
        self,
        source: Optional[StringFilter],
        request: Optional[RequestFilter],
        response: Optional[ResponseFilter],
    ):
        """Initialize RequestResponseFilter class instance."""
        self.source = source
        self.request = request
        self.response = response

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<RequestResponseFilter {self.name}>"
        elif hasattr(self, "id"):
            return f"<RequestResponseFilter {self.id}>"
        else:
            return f"<RequestResponseFilter>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate RequestResponseFilter instance from GraphQL query result."""
        instance = cls(
            source=response.get("source"),
            request=response.get("request"),
            response=response.get("response"),
        )

        return instance
