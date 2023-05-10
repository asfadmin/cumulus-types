# This is an auto-generated file. Do not modify by hand.

from typing import Any, Dict, List, Literal, TypedDict, Union

from typing_extensions import Required


class Config(TypedDict, total=False):
    """Config.

    Describes the config used by the move-granules task
    """

    bucket: Required[str]
    """The bucket the has the private/public key needed for decrypting cmr password.

    Required property
    """

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

    distribution_endpoint: Required[str]
    """The api distribution endpoint.

    Required property
    """

    collection: Required["_ConfigCollection"]
    """Required property."""

    moveStagedFiles: bool
    """Can set to false to skip moving files from the staging location.

    Defaults to true.
    """

    duplicateHandling: Literal["replace", "version", "skip", "error"]
    """Specifies how duplicate filenames should be handled. `error` will throw an error
    that, if not caught, will fail the task/workflow execution. `version` will add a
    suffix to the existing filename to avoid a clash.

    default: error
    """

    s3MultipartChunksizeMb: Union[Union[int, float], None]
    """S3 multipart upload chunk size in MB.

    If none is specified, the default default_s3_multipart_chunksize_mb
    is used.
    """


class _ConfigCollection(TypedDict, total=False):
    name: Required[str]
    """Required property."""

    process: str
    url_path: str
    duplicateHandling: str
    files: Required[List["_ConfigCollectionFilesItem"]]
    """Required property."""

    meta: Dict[str, Any]
    """Optional Metadata for the Collection."""


class _ConfigCollectionFilesItem(TypedDict, total=False):
    regex: Required[str]
    """Required property."""

    bucket: Required[str]
    """Required property."""

    url_path: str
