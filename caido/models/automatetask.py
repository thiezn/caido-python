#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .automateentry import AutomateEntry


class AutomateTask(BaseModel):
    """Class definition for AutomateTask."""

    def __init__(self, id: str, paused: bool, entry: AutomateEntry):
        """Initialize AutomateTask class instance."""
        self.id = id
        self.paused = paused
        self.entry = entry

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateTask {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateTask {self.id}>"
        else:
            return f"<AutomateTask>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateTask instance from GraphQL query result."""
        instance = cls(
            id=response["id"],
            paused=response["paused"],
            entry=response["entry"],
        )

        return instance
