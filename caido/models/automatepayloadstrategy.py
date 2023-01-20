#!/usr/bin/env python3

from enum import Enum


class AutomatePayloadStrategy(Enum):
    """Enum definition for AutomatePayloadStrategy."""

    ALL = "ALL"
    SEQUENTIAL = "SEQUENTIAL"
    PARALLEL = "PARALLEL"
    MATRIX = "MATRIX"
