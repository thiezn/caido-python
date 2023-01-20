#!/usr/bin/env python3

from enum import Enum


class IntFilterOperator(Enum):
    """Enum definition for IntFilterOperator."""

    LT = "LT"
    LTE = "LTE"
    GT = "GT"
    GTE = "GTE"
    EQ = "EQ"
    NE = "NE"
