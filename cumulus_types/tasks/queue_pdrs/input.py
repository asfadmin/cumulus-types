# This is an auto-generated file. Do not modify by hand.

from typing import List, TypedDict

from typing_extensions import Required


class Input(TypedDict, total=False):
    """Input.

    Describes the input expected by the queue-pdrs task
    """

    pdrs: Required[List["_InputPdrsItem"]]
    """Required property."""


class _InputPdrsItem(TypedDict, total=False):
    name: str
    path: str
