#!/usr/bin/env python3

from typing import Optional


class CancelAutomateTaskError:
    """Union definition for CancelAutomateTaskError."""

    unknown_id_user_error: Optional = None  # UnknownIdUserError
    other_user_error: Optional = None  # OtherUserError
