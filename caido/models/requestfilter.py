#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .intfilter import IntFilter
from .stringfilter import StringFilter


class RequestFilter(BaseModel):
    """Class definition for RequestFilter."""

    def __init__(
        self,
        file_extension: Optional[StringFilter],
        method: Optional[StringFilter],
        path: Optional[StringFilter],
        port: Optional[IntFilter],
        raw: Optional[StringFilter],
    ):
        """Initialize RequestFilter class instance."""
        self.file_extension = file_extension
        self.method = method
        self.path = path
        self.port = port
        self.raw = raw

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<RequestFilter {self.name}>"
        elif hasattr(self, "id"):
            return f"<RequestFilter {self.id}>"
        else:
            return f"<RequestFilter>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate RequestFilter instance from GraphQL query result."""
        instance = cls(
            file_extension=response.get("fileExtension"),
            method=response.get("method"),
            path=response.get("path"),
            port=response.get("port"),
            raw=response.get("raw"),
        )

        return instance
