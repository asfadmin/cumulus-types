# This is an auto-generated file. Do not modify by hand.

from typing import List, TypedDict

from typing_extensions import Required


class Output(TypedDict, total=False):
    """Output.

    Describes the output produced by the queue-pdrs task
    """

    running: Required[List[str]]
    """A list of step function execution arns of pdrs queued.

    Required property
    """

    pdrs_queued: Required[int]
    """Required property."""
