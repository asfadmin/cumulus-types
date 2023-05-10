# This is an auto-generated file. Do not modify by hand.

from typing import List, TypedDict

from typing_extensions import Required


class Config(TypedDict, total=False):
    """Config.

    Describes the config used by the files-to-granules task
    """

    inputGranules: Required[List["_ConfigInputgranulesItem"]]
    """Granules object used to construct output for cumulus indexer.

    Required property
    """

    granuleIdExtraction: str
    """The regex needed for extracting granuleId from filenames."""


class _ConfigInputgranulesItem(TypedDict, total=False):
    granuleId: Required[str]
    """Required property."""

    files: Required[List["_ConfigInputgranulesItemFilesItem"]]
    """Required property."""


class _ConfigInputgranulesItemFilesItem(TypedDict, total=False):
    bucket: Required[str]
    """Bucket in-process file is being staged in in S3.

    Required property
    """

    key: Required[str]
    """S3 Key for in-process file.

    Required property
    """
