#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .scope import Scope


class CreateScopePayload(BaseModel):
    """Class definition for CreateScopePayload."""

    def __init__(self, scope: Scope):
        """Initialize CreateScopePayload class instance."""
        self.scope = scope

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<CreateScopePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<CreateScopePayload {self.id}>"
        else:
            return f"<CreateScopePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate CreateScopePayload instance from GraphQL query result."""
        instance = cls(
            scope=response["scope"],
        )

        return instance
