#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .hostedfile import HostedFile


class RenameHostedFilePayload(BaseModel):
    """Class definition for RenameHostedFilePayload."""

    def __init__(self, hosted_file: Optional[HostedFile]):
        """Initialize RenameHostedFilePayload class instance."""
        self.hosted_file = hosted_file

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<RenameHostedFilePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<RenameHostedFilePayload {self.id}>"
        else:
            return f"<RenameHostedFilePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate RenameHostedFilePayload instance from GraphQL query result."""
        instance = cls(
            hosted_file=response.get("hostedFile"),
        )

        return instance
