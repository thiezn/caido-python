#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict


class OnboardingState(BaseModel):
    """Class definition for OnboardingState."""

    def __init__(self, license: bool, project: bool, ca_certificate: bool):
        """Initialize OnboardingState class instance."""
        self.license = license
        self.project = project
        self.ca_certificate = ca_certificate

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<OnboardingState {self.name}>"
        elif hasattr(self, "id"):
            return f"<OnboardingState {self.id}>"
        else:
            return f"<OnboardingState>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate OnboardingState instance from GraphQL query result."""
        instance = cls(
            license=response["license"],
            project=response["project"],
            ca_certificate=response["caCertificate"],
        )

        return instance
