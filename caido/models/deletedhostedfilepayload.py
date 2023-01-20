#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeletedHostedFilePayload(BaseModel):
    """Class definition for DeletedHostedFilePayload."""

    def __init__(self, deleted_hosted_file_id: str):
        """Initialize DeletedHostedFilePayload class instance."""
        self.deleted_hosted_file_id = deleted_hosted_file_id

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeletedHostedFilePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeletedHostedFilePayload {self.id}>"
        else:
            return f"<DeletedHostedFilePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeletedHostedFilePayload instance from GraphQL query result."""
        instance = cls(
            deleted_hosted_file_id=response["deletedHostedFileId"],
        )

        return instance
