# This is an auto-generated file. Do not modify by hand.

from typing import List, TypedDict

from typing_extensions import Required


class Input(TypedDict, total=False):
    """Input.

    Describes the input expected by the sync-granule task
    """

    granules: Required[List["_InputGranulesItem"]]
    """Required property."""


class _InputGranulesItem(TypedDict, total=False):
    granuleId: Required[str]
    """Required property."""

    dataType: str
    version: str
    files: Required[List["_InputGranulesItemFilesItem"]]
    """Required property."""


class _InputGranulesItemFilesItem(TypedDict, total=False):
    name: Required[str]
    """Name of file to be synced.

    Required property
    """

    filename: str
    """ optional field - usage depends on provider type """

    type: str
    source_bucket: str
    """ optional - alternate source bucket to use for this file instead of the provider bucket.  Works with s3 provider only, ignored for other providers """

    path: Required[str]
    """Provider path of file to be synced.

    Required property
    """
