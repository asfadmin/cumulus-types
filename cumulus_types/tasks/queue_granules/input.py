# This is an auto-generated file. Do not modify by hand.

from typing import List, TypedDict

from typing_extensions import Required


class Input(TypedDict, total=False):
    """Input.

    Describes the input and config used by the queue-granules task
    """

    pdr: "_InputPdr"
    granules: List["_InputGranulesItem"]


class _InputGranulesItem(TypedDict, total=False):
    type: str
    granuleId: Required[str]
    """Required property."""

    dataType: Required[str]
    """Required property."""

    version: Required[str]
    """Required property."""

    provider: str
    files: Required[None]
    """
    WARNING: we get an array without any items

    Required property
    """


class _InputPdr(TypedDict, total=False):
    name: Required[str]
    """Required property."""

    path: Required[str]
    """Required property."""
