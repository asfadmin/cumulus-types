# This is an auto-generated file. Do not modify by hand.

from typing import List, TypedDict, Union

from typing_extensions import Required


class Output(TypedDict, total=False):
    """Output.

    Describes the output expected by the LzardsBackup task component
    """

    backupResults: Required[List["_OutputBackupresultsItem"]]
    """Required property."""


class _OutputBackupresultsItem(TypedDict, total=False):
    body: str
    filename: Required[str]
    """Required property."""

    status: Required[str]
    """Required property."""

    granuleId: Required[str]
    """Required property."""

    statusCode: Union[int, float]
