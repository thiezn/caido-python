from typing import Dict


class BaseModel:
    """Base model representing objects in Caido GraphQL API."""

    @classmethod
    def from_graphql(cls, response: Dict):
        """Convert GraphQL response to model."""
        raise NotImplementedError

    def to_graphql(self):
        """Convert class instance to GraphQL model."""
        raise NotImplementedError
