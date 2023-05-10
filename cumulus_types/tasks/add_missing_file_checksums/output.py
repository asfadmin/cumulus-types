# This is an auto-generated file. Do not modify by hand.

from typing import List, TypedDict, Union

from typing_extensions import Required


class Output(TypedDict, total=False):
    """Output.

    Describes the output expected from the add-missing-file-checksums
    task
    """

    granules: Required[List["_OutputGranulesItem"]]
    """Required property."""


class _OutputGranulesItem(TypedDict, total=False):
    files: Required[List["_OutputGranulesItemFilesItem"]]
    """Required property."""


class _OutputGranulesItemFilesItem(TypedDict, total=False):
    bucket: Required[str]
    """Bucket where file is archived in S3.

    Required property
    """

    checksum: Required[str]
    """Checksum value for file.

    Required property
    """

    checksumType: Required[str]
    """Type of checksum (e.g. md5, sha256, etc)

    Required property
    """

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
