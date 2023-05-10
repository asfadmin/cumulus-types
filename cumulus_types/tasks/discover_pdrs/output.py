# This is an auto-generated file. Do not modify by hand.

from typing import List, TypedDict

from typing_extensions import Required


class Output(TypedDict, total=False):
    """Output.

    Describes the output produced by the discover-pdrs task
    """

    pdrs: Required[List["_OutputPdrsItem"]]
    """Required property."""


class _OutputPdrsItem(TypedDict, total=False):
    name: Required[str]
    """Required property."""

    path: Required[str]
    """Required property."""

    size: int
    time: int
    """The number of milliseconds since January 1, 1970, 00:00:00 UTC."""
