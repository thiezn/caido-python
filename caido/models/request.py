#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, List
from .source import Source
from .alteration import Alteration
from .response import Response


class Request(BaseModel):
    """Class definition for Request."""

    def __init__(
        self,
        id: str,
        host: str,
        method: str,
        path: str,
        query: str,
        length: int,
        port: int,
        is_tls: bool,
        source: Source,
        alteration: Alteration,
        edited: bool,
        raw: str,
        edits: List,
        file_extension: Optional[str],
        response: Optional[Response],
    ):
        """Initialize Request class instance."""
        self.id = id
        self.host = host
        self.method = method
        self.path = path
        self.query = query
        self.length = length
        self.port = port
        self.is_tls = is_tls
        self.source = source
        self.alteration = alteration
        self.edited = edited
        self.raw = raw
        self.edits = edits
        self.file_extension = file_extension
        self.response = response

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<Request {self.name}>"
        elif hasattr(self, "id"):
            return f"<Request {self.id}>"
        else:
            return f"<Request>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate Request instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            host=response["host"],
            method=response["method"],
            path=response["path"],
            query=response["query"],
            length=response["length"],
            port=response["port"],
            is_tls=response["isTls"],
            source=response["source"],
            alteration=response["alteration"],
            edited=response["edited"],
            raw=response["raw"],
            edits=response["edits"],
            file_extension=response.get("fileExtension"),
            response=response.get("response"),
        )

        return instance
