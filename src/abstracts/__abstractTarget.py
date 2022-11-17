from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractTarget(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_b(self, rsEntityId:str ='') -> str:
        pass
