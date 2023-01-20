#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .filteroptions import FilterOptions


class Filter(BaseModel):
    """Class definition for Filter."""

    def __init__(self, id: str, options: FilterOptions):
        """Initialize Filter class instance."""
        self.id = id
        self.options = options

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<Filter {self.name}>"
        elif hasattr(self, "id"):
            return f"<Filter {self.id}>"
        else:
            return f"<Filter>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate Filter instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            options=response["options"],
        )

        return instance
