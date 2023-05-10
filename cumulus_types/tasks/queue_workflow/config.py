# This is an auto-generated file. Do not modify by hand.

from typing import Any, Dict, TypedDict

from typing_extensions import Required


class Config(TypedDict, total=False):
    """Config.

    Describes the config used by the queue-workflow task
    """

    queueUrl: Required[str]
    """Required property."""

    internalBucket: Required[str]
    """Required property."""

    collection: Dict[str, Any]
    provider: Dict[str, Any]
    stackName: Required[str]
    """Required property."""

    executionNamePrefix: str
    workflow: Required[str]
    """Required property."""

    workflowInput: Dict[str, Any]
