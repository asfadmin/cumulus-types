# This is an auto-generated file. Do not modify by hand.

from typing import Literal, TypedDict

from typing_extensions import Required


class Config(TypedDict, total=False):
    """Config.

    Describes the config used by the discover-pdrs task
    """

    stack: Required[str]
    """The name of the Task's CloudFormation Task, useful as a prefix.

    Required property
    """

    provider: Required["_ConfigProvider"]
    """Required property."""

    bucket: Required[str]
    """Aws s3 buckets used by this task.

    Required property
    """

    useList: bool
    """Flag to tell ftp server to use 'LIST' instead of 'STAT'.

    default: False
    """

    httpListTimeout: int
    """Timeout (in seconds) for retrieval by HTTP/HTTPS provider.

    default: 300
    """

    force: bool
    """Flag to force the processing of PDR's that have already been discovered.

    default: False
    """

    filterPdrs: str
    provider_path: Required[str]
    """Required property."""


class _ConfigProvider(TypedDict, total=False):
    id: str
    username: str
    password: str
    host: str
    port: int
    globalConnectionLimit: int
    protocol: Literal["ftp", "sftp", "http", "https", "s3"]
