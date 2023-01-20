#!/usr/bin/env python3

from .basemodel import BaseModel
from typing import Optional, Dict, List
from .automateurlencodeoptions import AutomateUrlEncodeOptions
from .automatepayloadkind import AutomatePayloadKind
from .automatepayloadoptions import AutomatePayloadOptions


class AutomatePayload(BaseModel):
    """Class definition for AutomatePayload."""

    def __init__(
        self,
        options: AutomatePayloadOptions,
        preprocessors: List,
        url_encode: AutomateUrlEncodeOptions,
        kind: AutomatePayloadKind,
    ):
        """Initialize AutomatePayload class instance."""
        self.options = options
        self.preprocessors = preprocessors
        self.url_encode = url_encode
        self.kind = kind

    def __repr__(self) -> str:
        """Pretty class representation when printing."""
        if hasattr(self, "name"):
            return f"<AutomatePayload {self.name}>"
        elif hasattr(self, "id"):
            return f"<AutomatePayload {self.id}>"
        else:
            return f"<AutomatePayload>"

    @classmethod
    def from_graphql(cls, response: Dict):
        """Generate AutomatePayload instance from GraphQL query result."""
        instance = cls(
            options=response["options"],
            preprocessors=response["preprocessors"],
            url_encode=response["urlEncode"],
            kind=response["kind"],
        )

        return instance
