#!/usr/bin/env python3

from typing import Optional


class DeletedAutomateTaskError:
    """Union definition for DeletedAutomateTaskError."""

    automate_task_user_error: Optional = None  # AutomateTaskUserError
    other_user_error: Optional = None  # OtherUserError
