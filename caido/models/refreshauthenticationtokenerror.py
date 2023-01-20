#!/usr/bin/env python3

from typing import Optional


class RefreshAuthenticationTokenError:
    """Union definition for RefreshAuthenticationTokenError."""

    authentication_user_error: Optional = None  # AuthenticationUserError
    other_user_error: Optional = None  # OtherUserError
