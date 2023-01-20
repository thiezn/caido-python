#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class TaskInProgressUserError(BaseModel):
    """Class definition for TaskInProgressUserError."""

    def __init__(self, task_id: str, code: str):
        """Initialize TaskInProgressUserError class instance."""
        self.task_id = task_id
        self.code = code

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<TaskInProgressUserError {self.name}>"
        elif hasattr(self, "id"):
            return f"<TaskInProgressUserError {self.id}>"
        else:
            return f"<TaskInProgressUserError>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate TaskInProgressUserError instance from GraphQL query result."""
        instance = cls(
            task_id=response["taskId"],
            code=response["code"],
        )

        return instance
