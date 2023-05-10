# This is an auto-generated file. Do not modify by hand.

from typing import Any, Dict, TypedDict

from typing_extensions import Required


class Config(TypedDict, total=False):
    """Config.

    Describes the config used by the hyrax-metadata-updates task
    """

    cmr: Required["_ConfigCmr"]
    """Required property."""

    launchpad: "_ConfigLaunchpad"
    addShortnameAndVersionIdToConceptId: bool
    """Option to humanize the Hyrax URL. Humanizes when set to true.

    default: False
    """

    skipMetadataValidation: bool
    """Option to skip metadata validation.

    default: False
    """

    etags: Dict[str, Any]
    """Map of s3URIs to ETags."""


class _ConfigCmr(TypedDict, total=False):
    """Credentials needed to perform CMR searches and metadata validation."""

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
