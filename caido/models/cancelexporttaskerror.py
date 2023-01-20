#!/usr/bin/env python3

from typing import Optional


class CancelExportTaskError:
    """Union definition for CancelExportTaskError."""

    unknown_id_user_error: Optional = None  # UnknownIdUserError
    other_user_error: Optional = None  # OtherUserError
