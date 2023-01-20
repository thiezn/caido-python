#!/usr/bin/env python3

from enum import Enum


class AutomateTaskErrorReason(Enum):
    """Enum definition for AutomateTaskErrorReason."""

    INVALID_HOSTED_FILE = "INVALID_HOSTED_FILE"
    INTERNAL = "INTERNAL"
