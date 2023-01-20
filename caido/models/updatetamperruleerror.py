#!/usr/bin/env python3

from typing import Optional


class UpdateTamperRuleError:
    """Union definition for UpdateTamperRuleError."""

    unknown_id_user_error: Optional = None  # UnknownIdUserError
    invalid_regex_user_error: Optional = None  # InvalidRegexUserError
    other_user_error: Optional = None  # OtherUserError
