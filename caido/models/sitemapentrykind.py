#!/usr/bin/env python3

from enum import Enum


class SitemapEntryKind(Enum):
    """Enum definition for SitemapEntryKind."""

    DOMAIN = "DOMAIN"
    DIRECTORY = "DIRECTORY"
    REQUEST = "REQUEST"
    REQUEST_QUERY = "REQUEST_QUERY"
    REQUEST_BODY = "REQUEST_BODY"
