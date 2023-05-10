# This is an auto-generated file. Do not modify by hand.

from typing import Any, Dict, TypedDict

from typing_extensions import Required


class Output(TypedDict, total=False):
    """Output.

    Describes the output produced by the queue-workflow task
    """

    workflow: Required[str]
    """Required property."""

    workflowInput: Required[Dict[str, Any]]
    """Required property."""

    running: Required[str]
    """A step function execution arn of workflow queued.

    Required property
    """
