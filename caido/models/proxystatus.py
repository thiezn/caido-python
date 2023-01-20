#!/usr/bin/env python3

from enum import Enum


class ProxyStatus(Enum):
    """Enum definition for ProxyStatus."""

    PAUSED = "PAUSED"
    RUNNING = "RUNNING"
