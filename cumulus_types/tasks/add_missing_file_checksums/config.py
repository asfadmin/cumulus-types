# This is an auto-generated file. Do not modify by hand.

from typing import TypedDict

from typing_extensions import Required


class Config(TypedDict, total=False):
    """Config.

    Describes the config used by the add-missing-file-checksums task
    """

    algorithm: Required[str]
    """The algorithm to use for checksums.

    Required property
    """
