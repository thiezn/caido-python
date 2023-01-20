#!/usr/bin/env python3

from typing import Optional


class SelectProjectPayloadError:
    """Union definition for SelectProjectPayloadError."""

    project_locked_user_error: Optional = None  # ProjectLockedUserError
    other_user_error: Optional = None  # OtherUserError
