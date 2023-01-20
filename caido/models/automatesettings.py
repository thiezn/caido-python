#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, List
from .automateretryonfailuresetting import AutomateRetryOnFailureSetting
from .automateconcurrencysetting import AutomateConcurrencySetting
from .automatepayloadstrategy import AutomatePayloadStrategy


class AutomateSettings(BaseModel):
    """Class definition for AutomateSettings."""

    def __init__(
        self,
        payloads: List,
        placeholders: List,
        strategy: AutomatePayloadStrategy,
        retry_on_failure: AutomateRetryOnFailureSetting,
        close_connection: bool,
        update_content_length: bool,
        concurrency: Optional[AutomateConcurrencySetting],
    ):
        """Initialize AutomateSettings class instance."""
        self.payloads = payloads
        self.placeholders = placeholders
        self.strategy = strategy
        self.retry_on_failure = retry_on_failure
        self.close_connection = close_connection
        self.update_content_length = update_content_length
        self.concurrency = concurrency

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomateSettings {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomateSettings {self.id}>"
        else:
            return f"<AutomateSettings>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomateSettings instance from GraphQL query result."""
        instance = cls(
            payloads=response["payloads"],
            placeholders=response["placeholders"],
            strategy=response["strategy"],
            retry_on_failure=response["retryOnFailure"],
            close_connection=response["closeConnection"],
            update_content_length=response["updateContentLength"],
            concurrency=response.get("concurrency"),
        )

        return instance
