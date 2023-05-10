# This is an auto-generated file. Do not modify by hand.

from typing import Any, Dict, List, Literal, TypedDict

from typing_extensions import Required


class Config(TypedDict, total=False):
    """Config.

    Describes the config used by the sync-granule task
    """

    stack: str
    """The name of the deployment stack."""

    fileStagingDir: str
    """Directory used for staging location of files.

    Default is `file-staging`. Granules are further organized by stack
    name and collection name making the full path `file-staging/<stack
    name>/<collection name>`
    """

    provider: Required["_ConfigProvider"]
    """Required property."""

    buckets: Required[Dict[str, Any]]
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

    Required property
    """

    downloadBucket: Required[str]
    """AWS S3 bucket to use when downloading files.

    Required property
    """

    collection: "_ConfigCollection"
    pdr: Any
    """ WARNING: we get an schema without any type """

    duplicateHandling: Literal["replace", "version", "skip", "error"]
    """Specifies how duplicate filenames should be handled. `error` will throw an error
    that, if not caught, will fail the task/workflow execution. `version` will add a
    suffix to the existing filename to avoid a clash.

    default: error
    """

    syncChecksumFiles: bool
    """If true, checksum files are also synced. Default: false.

    default: False
    """

    workflowStartTime: int
    """Specifies the start time for the current workflow (as a timestamp) and will be
    used as the createdAt time for granules output."""


class _ConfigCollection(TypedDict, total=False):
    name: Required[str]
    """Required property."""

    process: str
    url_path: str
    duplicateHandling: str
    files: Required[List["_ConfigCollectionFilesItem"]]
    """Required property."""


class _ConfigCollectionFilesItem(TypedDict, total=False):
    regex: Required[str]
    """Required property."""

    bucket: Required[str]
    """Required property."""

    url_path: str


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
