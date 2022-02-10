from typing import Any, Dict
from kedro.io import AbstractDataSet, DataSetError

class xyzDataSet(AbstractDataSet):
    def __init__(self, filepath):
        self._filepath = filepath
    def _save(self, _):
        raise DataSetError("Read Only DataSet")
    def _load(self):
        with open(str(self._filepath), 'rb') as f:
            return f.read()
    def _describe(self):
        return dict(filpath=self._filepath)
