#!/usr/bin/env python3

from typing import Optional


class CreateTamperRuleError:
    """Union definition for CreateTamperRuleError."""

    invalid_regex_user_error: Optional = None  # InvalidRegexUserError
    other_user_error: Optional = None  # OtherUserError
