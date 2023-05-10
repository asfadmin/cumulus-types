import json
from typing import List, Sequence, Tuple

from jsonschema_gentypes import Type
from jsonschema_gentypes.api_draft_2020_12 import APIv202012


class LiteralType(Type):
    """
    A literal type like: `Literal["text"]`.
    """

    def __init__(self, values: Sequence) -> None:
        """
        Init.

        Arguments:
            const: the constant
        """
        super().__init__()
        self.values = values

    def name(self) -> str:
        """
        Return what we need to use the type.
        """
        values = [
            json.dumps(value) if isinstance(value, str) else value
            for value in self.values
        ]
        return f"Literal[{', '.join(values)}]"

    def imports(self, python_version: Tuple[int, ...]) -> List[Tuple[str, str]]:
        """
        Return the needed imports.
        """
        del python_version
        return [("typing", "Literal")]


class API(APIv202012):
    def enum(
        self,
        schema: dict,
        proposed_name: str,
    ) -> Type:
        """
        Generate an enum.
        """
        del proposed_name
        return LiteralType([value for value in schema["enum"]])
