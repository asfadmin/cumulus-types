# This is an auto-generated file. Do not modify by hand.

from typing import Any, Dict, TypedDict, Union

from typing_extensions import Required


class Config(TypedDict, total=False):
    """Config.

    Describes the config used by the queue-granules task
    """

    granuleIngestWorkflow: Required[str]
    """Required property."""

    internalBucket: Required[str]
    """Required property."""

    provider: Required[Dict[str, Any]]
    """Required property."""

    preferredQueueBatchSize: Union[Union[int, float], None]
    queueUrl: Required[str]
    """Required property."""

    stackName: Required[str]
    """Required property."""

    concurrency: Union[int, float]
    executionNamePrefix: str
    childWorkflowMeta: Dict[str, Any]
