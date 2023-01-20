#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict
from .onboardingstate import OnboardingState


class GlobalConfig(BaseModel):
    """Class definition for GlobalConfig."""

    def __init__(self, onboarding: OnboardingState, address: str):
        """Initialize GlobalConfig class instance."""
        self.onboarding = onboarding
        self.address = address

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<GlobalConfig {self.name}>"
        elif hasattr(self, "id"):
            return f"<GlobalConfig {self.id}>"
        else:
            return f"<GlobalConfig>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate GlobalConfig instance from GraphQL query result."""
        instance = cls(
            onboarding=response["onboarding"],
            address=response["address"],
        )

        return instance
