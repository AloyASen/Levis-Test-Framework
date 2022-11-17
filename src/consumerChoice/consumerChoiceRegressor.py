# impport the abstractions of the factory into this concrete factory creator
from ..abstracts import __abstractRegressor


#include the unit implementations for the duck typing created at parent 
from ._resourceTank import _FlexProductEvent
from ._getAPI__PIMproduct import _getPIMProduct
from ._comparator import _comparator
from ._reportSynidcator import _SyndicateReport

class ConsumerChoiceRegressorFactory(__abstractRegressor.AbstractRegressor):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_product_a(self) :
        return _FlexProductEvent()

    def create_product_b(self) :
        return _getPIMProduct()
    def create_comparator_AB(self) :
        return _comparator()
    def create_reportSyndicator(self) :
        return _SyndicateReport()

