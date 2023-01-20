#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .scope import Scope


class UpdateScopePayload(BaseModel):
    """Class definition for UpdateScopePayload."""

    def __init__(self, scope: Scope):
        """Initialize UpdateScopePayload class instance."""
        self.scope = scope

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<UpdateScopePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<UpdateScopePayload {self.id}>"
        else:
            return f"<UpdateScopePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate UpdateScopePayload instance from GraphQL query result."""
        instance = cls(
            scope=response["scope"],
        )

        return instance
