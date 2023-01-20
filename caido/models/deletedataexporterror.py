#!/usr/bin/env python3

from typing import Optional


class DeleteDataExportError:
    """Union definition for DeleteDataExportError."""

    task_in_progress_user_error: Optional = None  # TaskInProgressUserError
    other_user_error: Optional = None  # OtherUserError
