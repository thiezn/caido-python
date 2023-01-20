#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .hostedfile import HostedFile


class UploadHostedFilePayload(BaseModel):
    """Class definition for UploadHostedFilePayload."""

    def __init__(self, hosted_file: Optional[HostedFile]):
        """Initialize UploadHostedFilePayload class instance."""
        self.hosted_file = hosted_file

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UploadHostedFilePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UploadHostedFilePayload {self.id}>"
        else:
            return f"<UploadHostedFilePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UploadHostedFilePayload instance from GraphQL query result."""
        instance = cls(
            hosted_file=response.get("hostedFile"),
        )

        return instance
