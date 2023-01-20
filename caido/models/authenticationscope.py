#!/usr/bin/env python3

from enum import Enum


class AuthenticationScope(Enum):
    """Enum definition for AuthenticationScope."""

    OFFLINE = "OFFLINE"
    PROFILE_READ = "PROFILE_READ"
