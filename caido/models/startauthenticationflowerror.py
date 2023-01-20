#!/usr/bin/env python3

from typing import Optional


class StartAuthenticationFlowError:
    """Union definition for StartAuthenticationFlowError."""

    authentication_user_error: Optional = None  # AuthenticationUserError
    other_user_error: Optional = None  # OtherUserError
