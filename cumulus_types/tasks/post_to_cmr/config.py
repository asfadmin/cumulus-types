# This is an auto-generated file. Do not modify by hand.

from typing import Any, Dict, TypedDict

from typing_extensions import Required


class Config(TypedDict, total=False):
    """Config.

    Describes the config used by the post-to-cmr task
    """

    bucket: Required[str]
    """The bucket the has the private/public key needed for decrypting cmr password.

    Required property
    """

    stack: Required[str]
    """The name of the deployment stack.

    Required property
    """

    cmr: Required["_ConfigCmr"]
    """Required property."""

    launchpad: "_ConfigLaunchpad"
    skipMetaCheck: bool
    """Adds the option to allow PostToCMR to pass when processing a granule without a
    metadata file.

    default: False
    """

    etags: Dict[str, Any]
    """Map of s3URIs to ETags."""


class _ConfigCmr(TypedDict, total=False):
    """Credentials needed to post metadata to CMR."""

    oauthProvider: Required[str]
    """Required property."""

    provider: Required[str]
    """Required property."""

    clientId: Required[str]
    """Required property."""

    username: Required[str]
    """Required property."""

    passwordSecretName: Required[str]
    """Required property."""


class _ConfigLaunchpad(TypedDict, total=False):
    """Credentials needed to get launchpad token."""

    api: Required[str]
    """Required property."""

    passphraseSecretName: Required[str]
    """Required property."""

    certificate: Required[str]
    """Required property."""
