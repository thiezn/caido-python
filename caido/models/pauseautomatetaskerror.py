#!/usr/bin/env python3

from typing import Optional


class PauseAutomateTaskError:
    """Union definition for PauseAutomateTaskError."""

    unknown_id_user_error: Optional = None  # UnknownIdUserError
    other_user_error: Optional = None  # OtherUserError
