#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .hostedfile import HostedFile


class UpdatedHostedFilePayload(BaseModel):
    """Class definition for UpdatedHostedFilePayload."""

    def __init__(self, hosted_file: HostedFile):
        """Initialize UpdatedHostedFilePayload class instance."""
        self.hosted_file = hosted_file

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UpdatedHostedFilePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UpdatedHostedFilePayload {self.id}>"
        else:
            return f"<UpdatedHostedFilePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UpdatedHostedFilePayload instance from GraphQL query result."""
        instance = cls(
            hosted_file=response["hostedFile"],
        )

        return instance
