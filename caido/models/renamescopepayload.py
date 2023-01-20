#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .scope import Scope


class RenameScopePayload(BaseModel):
    """Class definition for RenameScopePayload."""

    def __init__(self, scope: Scope):
        """Initialize RenameScopePayload class instance."""
        self.scope = scope

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<RenameScopePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<RenameScopePayload {self.id}>"
        else:
            return f"<RenameScopePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate RenameScopePayload instance from GraphQL query result."""
        instance = cls(
            scope=response["scope"],
        )

        return instance
