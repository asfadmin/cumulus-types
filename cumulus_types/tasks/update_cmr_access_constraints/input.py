# This is an auto-generated file. Do not modify by hand.

from typing import List, TypedDict, Union

from typing_extensions import Required


class Input(TypedDict, total=False):
    """Input.

    Describes the input expected by the update-cmr-access-constraints
    task
    """

    granules: Required[List["_InputGranulesItem"]]
    """Array of all granules.

    Required property
    """


class _InputGranulesItem(TypedDict, total=False):
    granuleId: Required[str]
    """Required property."""

    files: Required[List["_InputGranulesItemFilesItem"]]
    """Required property."""


class _InputGranulesItemFilesItem(TypedDict, total=False):
    bucket: Required[str]
    """Bucket where file is archived in S3.

    Required property
    """

    checksum: str
    """Checksum value for file."""

    checksumType: str
    """Type of checksum (e.g. md5, sha256, etc)"""

    fileName: str
    """Name of file (e.g. file.txt)"""

    key: Required[str]
    """S3 Key for archived file.

    Required property
    """

    size: Union[int, float]
    """Size of file (in bytes)"""

    source: str
    """Source URI of the file from origin system (e.g. S3, FTP, HTTP)"""

    type: str
    """Type of file (e.g. data, metadata, browse)"""
