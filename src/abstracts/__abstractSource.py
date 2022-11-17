from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractSource(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_a(self,FilePath:str = None) -> str:
        pass
