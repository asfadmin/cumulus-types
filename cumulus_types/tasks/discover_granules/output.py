# This is an auto-generated file. Do not modify by hand.

from typing import List, TypedDict

from typing_extensions import Required


class Output(TypedDict, total=False):
    """Output.

    Describes the output produced by the discover-granules task
    """

    granules: Required[List["_OutputGranulesItem"]]
    """Required property."""


class _OutputGranulesItem(TypedDict, total=False):
    granuleId: Required[str]
    """Required property."""

    dataType: Required[str]
    """Required property."""

    version: Required[str]
    """Required property."""

    files: Required[List["_OutputGranulesItemFilesItem"]]
    """Required property."""


class _OutputGranulesItemFilesItem(TypedDict, total=False):
    name: Required[str]
    """The filename portion of path/filename.

    Required property
    """

    path: Required[str]
    """The path portion of path/filename.

    Required property
    """

    size: int
    type: str
    time: int
    """The number of milliseconds since January 1, 1970, 00:00:00 UTC."""

    bucket: str
    url_path: str
