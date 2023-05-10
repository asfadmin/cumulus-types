# This is an auto-generated file. Do not modify by hand.

from typing import TypedDict


class Config(TypedDict, total=False):
    """Config.

    Describes the configuration the hello-world task
    """

    fail: bool
    """True to throw an error for the task, failing the task."""

    passOnRetry: bool
    """If configured to fail, true to pass (not throw an error) when retried."""

    bucket: str
    """Bucket to write state information to handle the passOnRetry.

    Required if passOnRetry is true.
    """

    execution: str
    """Execution name, used to write state information for passOnRetry.

    Required if passOnRetry is true.
    """
