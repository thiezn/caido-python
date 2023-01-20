#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .filter import Filter


class View(BaseModel):
    """Class definition for View."""

    def __init__(self, id: str, scope_id: Optional[str], filter: Optional[Filter]):
        """Initialize View class instance."""
        self.id = id
        self.scope_id = scope_id
        self.filter = filter

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<View {self.name}>"
        elif hasattr(self, "id"):
            return f"<View {self.id}>"
        else:
            return f"<View>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate View instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            scope_id=response.get("scopeId"),
            filter=response.get("filter"),
        )

        return instance
