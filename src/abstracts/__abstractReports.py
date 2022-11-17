from __future__ import annotations
from abc import ABC, abstractmethod

from . import __abstractComparator

class AbstractReports(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass

    @abstractmethod
    def storeResults(self ):
        """
        ...but it also can collaborate with the ProductA.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass