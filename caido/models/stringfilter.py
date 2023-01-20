#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .stringfilteroperator import StringFilterOperator


class StringFilter(BaseModel):
    """Class definition for StringFilter."""

    def __init__(self, operator: StringFilterOperator, value: Optional[str]):
        """Initialize StringFilter class instance."""
        self.operator = operator
        self.value = value

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<StringFilter {self.name}>"
        elif hasattr(self, "id"):
            return f"<StringFilter {self.id}>"
        else:
            return f"<StringFilter>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate StringFilter instance from GraphQL query result."""
        instance = cls(
            operator=response["operator"],
            value=response.get("value"),
        )

        return instance
