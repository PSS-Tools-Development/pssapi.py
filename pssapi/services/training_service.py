from typing import List as _List

from .raw import TrainingServiceRaw as _TrainingServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import TrainingDesign as _TrainingDesign


class TrainingService(_ServiceBase):
    async def list_all_training_designs_2(self, language_key: str, design_version: int) -> _List[_TrainingDesign]:
        raise NotImplemented()
        result = await _TrainingServiceRaw.list_all_training_designs_2(self.production_server, language_key: str, design_version: int)
        return result


