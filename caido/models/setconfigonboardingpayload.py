#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .globalconfig import GlobalConfig


class SetConfigOnboardingPayload(BaseModel):
    """Class definition for SetConfigOnboardingPayload."""

    def __init__(self, config: GlobalConfig):
        """Initialize SetConfigOnboardingPayload class instance."""
        self.config = config

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<SetConfigOnboardingPayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<SetConfigOnboardingPayload {self.id}>"
        else:
            return f"<SetConfigOnboardingPayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate SetConfigOnboardingPayload instance from GraphQL query result."""
        instance = cls(
            config=response["config"],
        )

        return instance
