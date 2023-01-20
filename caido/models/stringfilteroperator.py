#!/usr/bin/env python3

from enum import Enum


class StringFilterOperator(Enum):
    """Enum definition for StringFilterOperator."""

    EQ = "EQ"
    NE = "NE"
    CONT = "CONT"
    NCONT = "NCONT"
    LIKE = "LIKE"
    NLIKE = "NLIKE"
