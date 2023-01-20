#!/usr/bin/env python3

from enum import Enum


class Source(Enum):
    """Enum definition for Source."""

    AUTOMATE = "AUTOMATE"
    INTERCEPT = "INTERCEPT"
    REPLAY = "REPLAY"
