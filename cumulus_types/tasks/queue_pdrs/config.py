# This is an auto-generated file. Do not modify by hand.

from typing import Any, Dict, TypedDict

from typing_extensions import Required


class Config(TypedDict, total=False):
    """Config.

    Describes the config used by the queue-pdrs task
    """

    collection: Required[Dict[str, Any]]
    """Required property."""

    provider: Required[Dict[str, Any]]
    """Required property."""

    queueUrl: Required[str]
    """Required property."""

    parsePdrWorkflow: Required[str]
    """Required property."""

    internalBucket: Required[str]
    """Required property."""

    stackName: Required[str]
    """Required property."""

    executionNamePrefix: str
    childWorkflowMeta: Dict[str, Any]
