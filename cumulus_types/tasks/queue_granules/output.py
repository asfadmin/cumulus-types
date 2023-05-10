# This is an auto-generated file. Do not modify by hand.

from typing import List, TypedDict

from typing_extensions import Required


class Output(TypedDict, total=False):
    """Output.

    Describes the output produced by the queue-granules task
    """

    running: Required[List[str]]
    """A list of step function execution arns of granules queued.

    Required property
    """

    pdr: "_OutputPdr"


class _OutputPdr(TypedDict, total=False):
    """Product Delivery Record."""

    name: Required[str]
    """Required property."""

    path: Required[str]
    """Required property."""
