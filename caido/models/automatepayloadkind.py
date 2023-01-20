#!/usr/bin/env python3

from enum import Enum


class AutomatePayloadKind(Enum):
    """Enum definition for AutomatePayloadKind."""

    SIMPLE_LIST = "SIMPLE_LIST"
    HOSTED_FILE = "HOSTED_FILE"
    NULL = "NULL"
