from ..abstracts import __abstractReports
import pandas as pd

"""
Concrete Products are created by corresponding Concrete Factories.
"""


class _SyndicateReport(__abstractReports.AbstractReports):
    def useful_function_a(self):
        pass
    def __init__(self) -> None:
        super().__init__()
    def storeResults(self, *args, **kwargs):
        # forward it to store the result into xls
        return self._storeToXLS( *args, **kwargs)
    def _storeToXLS(self, payload:list = [], blobstore:str='' ):
        df = pd.DataFrame.from_dict(payload)
        df.to_excel(blobstore)
        return('result blob storage successfully created: ', blobstore)
