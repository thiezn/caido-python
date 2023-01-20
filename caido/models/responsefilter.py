#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .intfilter import IntFilter
from .stringfilter import StringFilter


class ResponseFilter(BaseModel):
    """Class definition for ResponseFilter."""

    def __init__(self, raw: Optional[StringFilter], status_code: Optional[IntFilter]):
        """Initialize ResponseFilter class instance."""
        self.raw = raw
        self.status_code = status_code

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<ResponseFilter {self.name}>"
        elif hasattr(self, "id"):
            return f"<ResponseFilter {self.id}>"
        else:
            return f"<ResponseFilter>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate ResponseFilter instance from GraphQL query result."""
        instance = cls(
            raw=response.get("raw"),
            status_code=response.get("statusCode"),
        )

        return instance
