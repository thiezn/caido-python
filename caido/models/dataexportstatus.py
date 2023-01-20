#!/usr/bin/env python3

from enum import Enum


class DataExportStatus(Enum):
    """Enum definition for DataExportStatus."""

    DONE = "DONE"
    PROCESSING = "PROCESSING"
    ERROR = "ERROR"
    CANCELLED = "CANCELLED"
