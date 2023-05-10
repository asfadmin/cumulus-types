# This is an auto-generated file. Do not modify by hand.

from typing import Any, Dict, List, Literal, TypedDict, Union

from typing_extensions import Required


class Config(TypedDict, total=False):
    """Config.

    Describes the config used by the discover-granules task
    """

    provider: Required["_ConfigProvider"]
    """Required property."""

    provider_path: Required[str]
    """Required property."""

    buckets: Dict[str, Any]
    """Aws s3 buckets used by this task.

    patternProperties:
      \S*:
        description: bucket configuration for the key'd bucket
        properties:
          name:
            description: name of the S3 bucket
            type: string
          type:
            description: the type of bucket - i.e. internal, public, private, protected
            type: string
        type: object
    """

    collection: "_ConfigCollection"
    ignoreFilesConfigForDiscovery: bool
    """Overrides this property for all collections.

    See same property name at collection level.
    """

    useList: bool
    """Flag to tell ftp server to use 'LIST' instead of 'STAT'.

    default: False
    """

    httpListTimeout: int
    """Timeout (in seconds) for retrieval by HTTP/HTTPS provider.

    default: 300
    """

    duplicateGranuleHandling: str
    """Flag to set DiscoverGranules duplicate handling behavior.

    default: replace
    """

    concurrency: Union[int, float]
    """Concurrency used when querying Cumulus API for already discovered granules.

    default: 3
    """


class _ConfigCollection(TypedDict, total=False):
    name: Required[str]
    """Required property."""

    version: Required[str]
    """Required property."""

    url_path: str
    granuleId: str
    sampleFileName: str
    granuleIdExtraction: str
    ignoreFilesConfigForDiscovery: bool
    """When true, ignore this collection's files config list for determining which files
    to ingest for a granule, and ingest them all.  Otherwise, ingest only files that
    match a regex in one of this collection's files config list.  When this property is
    specified on a task, it overrides the value set on the collection.

    default: False
    """

    files: Required[List["_ConfigCollectionFilesItem"]]
    """Required property."""


class _ConfigCollectionFilesItem(TypedDict, total=False):
    regex: str
    sampleFileName: str
    bucket: str


class _ConfigProvider(TypedDict, total=False):
    id: str
    username: str
    password: str
    host: Required[str]
    """Required property."""

    port: int
    globalConnectionLimit: int
    protocol: Required[Literal["ftp", "sftp", "http", "https", "s3"]]
    """Required property."""
