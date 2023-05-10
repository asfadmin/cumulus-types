# This is an auto-generated file. Do not modify by hand.

from typing import Any, Dict, TypedDict, Union

from typing_extensions import Required


class Config(TypedDict, total=False):
    """Config.

    Describes the config used by the update-cmr-access-constraints task
    """

    accessConstraints: Required["_ConfigAccessconstraints"]
    """Required property."""

    etags: Dict[str, Any]
    """Map of s3URIs to ETags."""


class _ConfigAccessconstraints(TypedDict, total=False):
    """Object containing CMR access constraint value and description."""

    value: Required[Union[int, float]]
    """Required property."""

    description: str
