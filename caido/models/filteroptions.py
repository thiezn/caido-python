#!/usr/bin/env python3

from typing import Optional


class FilterOptions:
    """Union definition for FilterOptions."""

    request_response_filter: Optional = None  # RequestResponseFilter
    intercept_entry_filter: Optional = None  # InterceptEntryFilter
