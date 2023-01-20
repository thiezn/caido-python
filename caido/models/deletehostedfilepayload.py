#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class DeleteHostedFilePayload(BaseModel):
    """Class definition for DeleteHostedFilePayload."""

    def __init__(self, deleted_id: Optional[str]):
        """Initialize DeleteHostedFilePayload class instance."""
        self.deleted_id = deleted_id

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<DeleteHostedFilePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<DeleteHostedFilePayload {self.id}>"
        else:
            return f"<DeleteHostedFilePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate DeleteHostedFilePayload instance from GraphQL query result."""
        instance = cls(
            deleted_id=response.get("deletedId"),
        )

        return instance
