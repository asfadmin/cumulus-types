# This is an auto-generated file. Do not modify by hand.

from typing import List, TypedDict

from typing_extensions import Required


class Output(TypedDict, total=False):
    """Output.

    Describes the output produced by the pdr-status-check task
    """

    running: Required[List[str]]
    """List of execution arns which are queued or running.

    Required property
    """

    completed: Required[List[str]]
    """List of completed execution arns.

    Required property
    """

    failed: Required[List["_OutputFailedItem"]]
    """List of failed execution arns with reason.

    Required property
    """

    counter: int
    limit: int
    isFinished: Required[bool]
    """Indicates whether all the step function executions of the PDR are in terminal
    states.

    Required property
    """

    pdr: Required["_OutputPdr"]
    """Required property."""


class _OutputFailedItem(TypedDict, total=False):
    arn: Required[str]
    """Required property."""

    reason: Required[str]
    """Required property."""


class _OutputPdr(TypedDict, total=False):
    """Product Delivery Record."""

    name: Required[str]
    """Required property."""

    path: Required[str]
    """Required property."""
