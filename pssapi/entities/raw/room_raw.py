####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class RoomRaw():
    XML_NODE_NAME: str = 'Room'

    def __init__(self, room_info: _EntityInfo) -> None:
        self.__power_generated: int = _parse.pss_int(room_info.get('PowerGenerated'))
        self.__row: int = _parse.pss_int(room_info.get('Row'))
        self.__column: int = _parse.pss_int(room_info.get('Column'))
        self.__previous_skin_key: int = _parse.pss_int(room_info.get('PreviousSkinKey'))
        self.__salvage_string: str = _parse.pss_str(room_info.get('SalvageString'))
        self.__item_ids: str = _parse.pss_str(room_info.get('ItemIds'))
        self.__construction_start_date: str = _parse.pss_str(room_info.get('ConstructionStartDate'))
        self.__room_id: int = _parse.pss_int(room_info.get('RoomId'))
        self.__manufacture_string: str = _parse.pss_str(room_info.get('ManufactureString'))
        self.__target_manufacture_string: str = _parse.pss_str(room_info.get('TargetManufactureString'))
        self.__room_status: str = _parse.pss_str(room_info.get('RoomStatus'))
        self.__room_design_id: int = _parse.pss_int(room_info.get('RoomDesignId'))
        self.__manufactured: int = _parse.pss_int(room_info.get('Manufactured'))
        self.__capacity_used: int = _parse.pss_int(room_info.get('CapacityUsed'))
        self.__upgrade_room_design_id: int = _parse.pss_int(room_info.get('UpgradeRoomDesignId'))
        self.__random_seed: int = _parse.pss_int(room_info.get('RandomSeed'))
        self.__ship_id: int = _parse.pss_int(room_info.get('ShipId'))
        self.__manufacture_start_date: str = _parse.pss_str(room_info.get('ManufactureStartDate'))
        self.__current_skin_key: int = _parse.pss_int(room_info.get('CurrentSkinKey'))

    @property
    def power_generated(self) -> int:
        return self.__power_generated

    @property
    def row(self) -> int:
        return self.__row

    @property
    def column(self) -> int:
        return self.__column

    @property
    def previous_skin_key(self) -> int:
        return self.__previous_skin_key

    @property
    def salvage_string(self) -> str:
        return self.__salvage_string

    @property
    def item_ids(self) -> str:
        return self.__item_ids

    @property
    def construction_start_date(self) -> str:
        return self.__construction_start_date

    @property
    def room_id(self) -> int:
        return self.__room_id

    @property
    def manufacture_string(self) -> str:
        return self.__manufacture_string

    @property
    def target_manufacture_string(self) -> str:
        return self.__target_manufacture_string

    @property
    def room_status(self) -> str:
        return self.__room_status

    @property
    def room_design_id(self) -> int:
        return self.__room_design_id

    @property
    def manufactured(self) -> int:
        return self.__manufactured

    @property
    def capacity_used(self) -> int:
        return self.__capacity_used

    @property
    def upgrade_room_design_id(self) -> int:
        return self.__upgrade_room_design_id

    @property
    def random_seed(self) -> int:
        return self.__random_seed

    @property
    def ship_id(self) -> int:
        return self.__ship_id

    @property
    def manufacture_start_date(self) -> str:
        return self.__manufacture_start_date

    @property
    def current_skin_key(self) -> int:
        return self.__current_skin_key