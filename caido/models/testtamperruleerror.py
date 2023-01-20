#!/usr/bin/env python3

from typing import Optional


class TestTamperRuleError:
    """Union definition for TestTamperRuleError."""

    invalid_regex_user_error: Optional = None  # InvalidRegexUserError
    other_user_error: Optional = None  # OtherUserError
