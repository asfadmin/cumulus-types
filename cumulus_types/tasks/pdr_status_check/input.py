# This is an auto-generated file. Do not modify by hand.

from typing import List, TypedDict

from typing_extensions import Required


class Input(TypedDict, total=False):
    """Input.

    Describes the input expected by the pdr-status-check task
    """

    running: Required[List[str]]
    """List of execution arns which are queued or running.

    Required property
    """

    completed: List[str]
    """List of completed execution arns."""

    failed: List["_InputFailedItem"]
    """List of failed execution arns with reason."""

    counter: int
    limit: int
    isFinished: bool
    """Indicates whether all the step function executions of the PDR are in terminal
    states."""

    pdr: Required["_InputPdr"]
    """Required property."""


class _InputFailedItem(TypedDict, total=False):
    arn: Required[str]
    """Required property."""

    reason: Required[str]
    """Required property."""


class _InputPdr(TypedDict, total=False):
    """Product Delivery Record."""

    name: Required[str]
    """Required property."""

    path: Required[str]
    """Required property."""
