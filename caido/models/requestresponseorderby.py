#!/usr/bin/env python3

from enum import Enum


class RequestResponseOrderBy(Enum):
    """Enum definition for RequestResponseOrderBy."""

    ID = "ID"
    HOST = "HOST"
    METHOD = "METHOD"
    PATH = "PATH"
    STATUS_CODE = "STATUS_CODE"
