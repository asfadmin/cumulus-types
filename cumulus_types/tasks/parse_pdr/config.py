# This is an auto-generated file. Do not modify by hand.

from typing import Literal, TypedDict

from typing_extensions import Required


class Config(TypedDict, total=False):
    """Config.

    Describes the config used by the parse-pdr task
    """

    pdrFolder: str
    stack: Required[str]
    """The name of the Task's CloudFormation Task, useful as a prefix.

    Required property
    """

    granuleIdFilter: str
    """A regular expression that is applied against the filename of the first file of
    each granule contained in the PDR.

    If the regular expression matches, then the granule is included in
    the output.  Defaults to '.', which will match all granules in the
    PDR.
    """

    provider: Required["_ConfigProvider"]
    """Required property."""

    bucket: Required[str]
    """Required property."""

    useList: bool
    """Flag to tell ftp server to use 'LIST' instead of 'STAT'.

    default: False
    """


class _ConfigProvider(TypedDict, total=False):
    id: str
    globalConnectionLimit: int
    protocol: Literal["ftp", "sftp", "http", "https", "s3"]
