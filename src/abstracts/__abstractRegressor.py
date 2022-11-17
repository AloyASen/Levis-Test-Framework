from __future__ import annotations
from abc import ABC, abstractmethod

from . import __abstractSource
from . import __abstractTarget
from . import __abstractComparator
from . import __abstractReports

class AbstractRegressor(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """
    @abstractmethod
    def create_product_a(self) -> __abstractSource.AbstractSource:
        pass

    @abstractmethod
    def create_product_b(self) -> __abstractTarget.AbstractTarget:
        pass

    @abstractmethod
    def create_comparator_AB(self) -> __abstractComparator.AbstractComparator :
        pass

    @abstractmethod
    def create_reportSyndicator(self) -> __abstractReports.AbstractReports :
        pass


