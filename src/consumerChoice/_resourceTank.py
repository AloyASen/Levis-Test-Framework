from ..abstracts import __abstractSource
import json

"""
Concrete Products are created by corresponding Concrete Factories.
"""


class _FlexProductEvent(__abstractSource.AbstractSource):
    def useful_function_a(self, FilePath:str = None) -> str:
        JSON = []
        with open(FilePath) as f:
            JSON = json.load(f)
        return JSON