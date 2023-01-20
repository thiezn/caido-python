#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .intfilteroperator import IntFilterOperator


class IntFilter(BaseModel):
    """Class definition for IntFilter."""

    def __init__(self, operator: IntFilterOperator, value: Optional[int]):
        """Initialize IntFilter class instance."""
        self.operator = operator
        self.value = value

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<IntFilter {self.name}>"
        elif hasattr(self, "id"):
            return f"<IntFilter {self.id}>"
        else:
            return f"<IntFilter>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate IntFilter instance from GraphQL query result."""
        instance = cls(
            operator=response["operator"],
            value=response.get("value"),
        )

        return instance
