# This is an auto-generated file. Do not modify by hand.

from typing import Literal, TypedDict


class Config(TypedDict, total=False):
    """Config.

    Describes config options for the LZARDS backup task
    """

    urlType: Literal["s3", "cloudfront"]
    """The type of access URL to pass to LZARDS: S3 direct access OR cloudfront.

    default: s3
    """

    cloudfrontEndpoint: str
    """Cloudfront endpoint URL/host.

    Required if urlType is cloudfront
    """
