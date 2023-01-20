#!/usr/bin/env python3

from typing import Optional


class ResumeAutomateTaskError:
    """Union definition for ResumeAutomateTaskError."""

    unknown_id_user_error: Optional = None  # UnknownIdUserError
    other_user_error: Optional = None  # OtherUserError
