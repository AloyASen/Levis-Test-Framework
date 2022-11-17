from __future__ import annotations
from abc import ABC, abstractmethod

from . import __abstractSource
from . import __abstractTarget

class AbstractComparator(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


    @abstractmethod
    def _comparator(self, collaborator_a: __abstractSource.AbstractSource , collaborator_b: __abstractTarget.AbstractTarget ) -> None:
        """
        ...but it also can collaborate with the ProductA.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass