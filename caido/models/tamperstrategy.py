#!/usr/bin/env python3

from enum import Enum


class TamperStrategy(Enum):
    """Enum definition for TamperStrategy."""

    REQUEST_FIRST_LINE = "REQUEST_FIRST_LINE"
    REQUEST_HEADER = "REQUEST_HEADER"
    REQUEST_BODY = "REQUEST_BODY"
    RESPONSE_FIRST_LINE = "RESPONSE_FIRST_LINE"
    RESPONSE_HEADER = "RESPONSE_HEADER"
    RESPONSE_BODY = "RESPONSE_BODY"
