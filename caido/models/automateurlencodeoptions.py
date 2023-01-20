#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class AutomateUrlEncodeOptions(BaseModel):
    """Class definition for AutomateUrlEncodeOptions."""

    def __init__(self, enabled: bool, non_ascii: bool, charset: Optional[str]):
        """Initialize AutomateUrlEncodeOptions class instance."""
        self.enabled = enabled
        self.non_ascii = non_ascii
        self.charset = charset

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateUrlEncodeOptions {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateUrlEncodeOptions {self.id}>"
        else:
            return f"<AutomateUrlEncodeOptions>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateUrlEncodeOptions instance from GraphQL query result."""
        instance = cls(
            enabled=response["enabled"],
            non_ascii=response["nonAscii"],
            charset=response.get("charset"),
        )

        return instance
