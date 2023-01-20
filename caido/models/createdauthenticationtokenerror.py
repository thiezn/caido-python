#!/usr/bin/env python3

from typing import Optional


class CreatedAuthenticationTokenError:
    """Union definition for CreatedAuthenticationTokenError."""

    authentication_user_error: Optional = None  # AuthenticationUserError
    other_user_error: Optional = None  # OtherUserError
