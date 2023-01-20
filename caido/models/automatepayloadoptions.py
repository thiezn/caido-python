#!/usr/bin/env python3

from typing import Optional


class AutomatePayloadOptions:
    """Union definition for AutomatePayloadOptions."""

    automate_simple_list_payload: Optional = None  # AutomateSimpleListPayload
    automate_hosted_file_payload: Optional = None  # AutomateHostedFilePayload
    automate_null_payload: Optional = None  # AutomateNullPayload
