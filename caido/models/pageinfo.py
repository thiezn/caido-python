#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class PageInfo(BaseModel):
    """Information about pagination in a connection."""

    def __init__(
        self,
        has_previous_page: bool,
        has_next_page: bool,
        start_cursor: Optional[str],
        end_cursor: Optional[str],
    ):
        """Initialize PageInfo class instance."""
        self.has_previous_page = has_previous_page
        self.has_next_page = has_next_page
        self.start_cursor = start_cursor
        self.end_cursor = end_cursor

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<PageInfo {self.name}>"
        elif hasattr(self, "id"):
            return f"<PageInfo {self.id}>"
        else:
            return f"<PageInfo>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate PageInfo instance from GraphQL query result."""
        instance = cls(
            has_previous_page=response["hasPreviousPage"],
            has_next_page=response["hasNextPage"],
            start_cursor=response.get("startCursor"),
            end_cursor=response.get("endCursor"),
        )

        return instance
