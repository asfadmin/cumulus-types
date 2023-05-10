# This is an auto-generated file. Do not modify by hand.

from typing import List, TypedDict, Union

from typing_extensions import Required


class Output(TypedDict, total=False):
    """Output.

    Describes the output produced by the parse-pdr task
    """

    filesCount: Union[int, float]
    totalSize: Union[int, float]
    granulesCount: Union[int, float]
    pdr: "_OutputPdr"
    granules: List["_OutputGranulesItem"]


class _OutputGranulesItem(TypedDict, total=False):
    granuleId: str
    dataType: str
    granuleSize: Union[int, float]
    granuleCount: Union[int, float]
    filesCount: Union[int, float]
    totalSize: Union[int, float]
    files: List["_OutputGranulesItemFilesItem"]


class _OutputGranulesItemFilesItem(TypedDict, total=False):
    path: str
    name: str
    type: str
    size: Union[int, float]
    checksumType: str
    checksum: Union[str, Union[int, float]]


class _OutputPdr(TypedDict, total=False):
    name: Required[str]
    """Required property."""

    path: Required[str]
    """Required property."""
