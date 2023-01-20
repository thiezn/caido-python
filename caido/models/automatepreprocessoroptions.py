#!/usr/bin/env python3

from typing import Optional


class AutomatePreprocessorOptions:
    """Union definition for AutomatePreprocessorOptions."""

    automate_prefix_preprocessor: Optional = None  # AutomatePrefixPreprocessor
    automate_suffix_preprocessor: Optional = None  # AutomateSuffixPreprocessor
