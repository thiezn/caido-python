#!/usr/bin/env python3

from typing import Optional


class CreateProjectPayloadError:
    """Union definition for CreateProjectPayloadError."""

    name_taken_user_error: Optional = None  # NameTakenUserError
    other_user_error: Optional = None  # OtherUserError
