#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .hostedfile import HostedFile


class UploadedHostedFilePayload(BaseModel):
    """Class definition for UploadedHostedFilePayload."""

    def __init__(self, hosted_file: HostedFile):
        """Initialize UploadedHostedFilePayload class instance."""
        self.hosted_file = hosted_file

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UploadedHostedFilePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UploadedHostedFilePayload {self.id}>"
        else:
            return f"<UploadedHostedFilePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UploadedHostedFilePayload instance from GraphQL query result."""
        instance = cls(
            hosted_file=response["hostedFile"],
        )

        return instance
