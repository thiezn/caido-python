#!/usr/bin/env python3

from typing import Optional


class DeleteAutomateEntryError:
    """Union definition for DeleteAutomateEntryError."""

    task_in_progress_user_error: Optional = None  # TaskInProgressUserError
    other_user_error: Optional = None  # OtherUserError
