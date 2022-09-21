from typing import List as _List

from .raw import TrainingServiceRaw as _TrainingServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import TrainingDesign as _TrainingDesign


class TrainingService(_ServiceBase, _TrainingServiceRaw):
    async def list_all_training_designs_2(self, **params) -> _List[_TrainingDesign]:
        return await self._list_all_training_designs_2(self.production_server, self.language_key, **params)

    def __repr__(self) -> str:
        return f'<TrainingService: {self.name}>'

    def __str__(self) -> str:
        return f'<TrainingService: {self.name}>'
