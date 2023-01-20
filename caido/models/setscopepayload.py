#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .view import View


class SetScopePayload(BaseModel):
    """Class definition for SetScopePayload."""

    def __init__(self, view: View):
        """Initialize SetScopePayload class instance."""
        self.view = view

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<SetScopePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<SetScopePayload {self.id}>"
        else:
            return f"<SetScopePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate SetScopePayload instance from GraphQL query result."""
        instance = cls(
            view=response["view"],
        )

        return instance
