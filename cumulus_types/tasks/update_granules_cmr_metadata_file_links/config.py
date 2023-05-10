# This is an auto-generated file. Do not modify by hand.

from typing import Any, Dict, Literal, TypedDict

from typing_extensions import Required


class Config(TypedDict, total=False):
    """Config.

    Describes the config used by the update-granules-cmr-metadata-file-
    links task
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

    etags: Dict[str, Any]
    """Map of s3URIs to ETags."""

    cmrGranuleUrlType: Literal["distribution", "s3", "both", "none"]
    """The type of URL to add to the Online Access URLs in the CMR file. 'distribution'
    to point to the distribution API, 's3' to put in the S3 link, and 'none' to not add
    Online Access URLs for the granules.

    default: both
    """
