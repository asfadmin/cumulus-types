# This is an auto-generated file. Do not modify by hand.

from typing import TypedDict

from typing_extensions import Required


class Output(TypedDict, total=False):
    """Output.

    Describes the output produced by the hello-world task
    """

    hello: Required[str]
    """Required property."""
