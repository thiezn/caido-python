#!/usr/bin/env python3

from enum import Enum


class AuthenticationErrorReason(Enum):
    """Enum definition for AuthenticationErrorReason."""

    EXPIRED = "EXPIRED"
    DENIED = "DENIED"
    INVALID = "INVALID"
    CLOUD_UNAVAILABLE = "CLOUD_UNAVAILABLE"
    CLOUD_ERROR = "CLOUD_ERROR"
    INTERNAL = "INTERNAL"
