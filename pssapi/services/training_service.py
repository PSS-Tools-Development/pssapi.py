from typing import List as _List

from .raw import TrainingServiceRaw as _TrainingServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import TrainingDesign as _TrainingDesign


class TrainingService(_ServiceBase):
    async def list_all_training_designs(self, design_version: int = None) -> _List[_TrainingDesign]:
        result = await _TrainingServiceRaw.list_all_training_designs_2(production_server=self.production_server, design_version=design_version, language_key=self.language_key)
        return result
