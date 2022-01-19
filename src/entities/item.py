from datetime import timedelta as _timedelta
import json as _json
from typing import Any as _Any
from typing import Dict as _Dict
from typing import Tuple as _Tuple

from .entity_base import EntityBase as _EntityBase
from .raw import ItemDesignRaw as _ItemDesignRaw
from ..enums import CharacterPartType as _CharacterPartType
from ..enums import EnhancementType as _EnhancementType
from ..enums import ItemDesignFlag as _ItemDesignFlag
from ..enums import ItemSubType as _ItemSubType
from ..enums import ItemType as _ItemType
from ..enums import ModuleType as _ModuleType
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse


####################################################################################
##   This file will be generated with a class stub on the first code generation   ##
####################################################################################


class ItemDesign(_EntityBase, _ItemDesignRaw):
    def __init__(self, item_design_info: _EntityInfo) -> None:
        super(_ItemDesignRaw).__init__(item_design_info)
        self.__item_design_flags: ItemDesignFlags = ItemDesignFlags(self.__flags)
        self.__item_design_metadata: ItemDesignMetadata = ItemDesignMetadata(self.__metadata)


    @property
    def id(self) -> int:
        return self.item_design_id


    @property
    def character_part_type(self) -> _CharacterPartType:
        """
        Not sure what to do about these.
        Overwrite the property? (unexpected)
        Or make a new property 'item_design_character_part_type'? (very long name)
        Or make a new property 'character_part_type_'? (meaning unclear)
        """
        pass


    @property
    def item_design_flags(self) -> 'ItemDesignFlags':
        return self.__item_design_flags


    @property
    def item_design_metadata(self) -> 'ItemDesignMetadata':
        return self.__item_design_metadata





class ItemDesignFlags():
    def __init__(self, flags: int):
        self.__allow_trading: bool = flags & _ItemDesignFlag.AllowTrading or False
        self.__dropship_reward: bool = flags & _ItemDesignFlag.DropshipReward or False
        self.__challenge_reward: bool = flags & _ItemDesignFlag.ChallengeReward or False
        self.__pvp_reward: bool = flags & _ItemDesignFlag.PvpReward or False
        self.__instant_reward: bool = flags & _ItemDesignFlag.InstantReward or False
        self.__mission_reward: bool = flags & _ItemDesignFlag.MissionReward or False
        self.__consumable: bool = flags & _ItemDesignFlag.Consumable or False
        self.__align_to_top: bool = flags & _ItemDesignFlag.AlignToTop or False
        self.__allow_donation: bool = flags & _ItemDesignFlag.AllowDonation or False
        self.__giftable: bool = flags & _ItemDesignFlag.Giftable or False
        self.__use_on_crew: bool = flags & _ItemDesignFlag.UseOnCrew or False
        self.__recycling_build: bool = flags & _ItemDesignFlag.RecyclingBuild or False
        self.__used_item: bool = flags & _ItemDesignFlag.UsedItem or False
        self.__allow_manufacture: bool = flags & _ItemDesignFlag.AllowManufacture or False
        self.__task_prize: bool = flags & _ItemDesignFlag.TaskPrize or False
        self.__unique_content_reward: bool = flags & _ItemDesignFlag.UniqueContentReward or False
        self.__use_on_room: bool = flags & _ItemDesignFlag.UseOnRoom or False

    @property
    def align_to_top(self) -> bool:
        return self.__align_to_top

    @property
    def allow_donation(self) -> bool:
        return self.__allow_donation

    @property
    def allow_manufacture(self) -> bool:
        return self.__allow_manufacture

    @property
    def allow_trading(self) -> bool:
        return self.__allow_trading

    @property
    def challenge_reward(self) -> bool:
        return self.__challenge_reward

    @property
    def consumable(self) -> bool:
        return self.__consumable

    @property
    def dropship_reward(self) -> bool:
        return self.__dropship_reward

    @property
    def giftable(self) -> bool:
        return self.__giftable

    @property
    def instant_reward(self) -> bool:
        return self.__instant_reward

    @property
    def mission_reward(self) -> bool:
        return self.__mission_reward

    @property
    def pvp_reward(self) -> bool:
        return self.__pvp_reward

    @property
    def recycling_build(self) -> bool:
        return self.__recycling_build

    @property
    def task_prize(self) -> bool:
        return self.__task_prize

    @property
    def unique_content_reward(self) -> bool:
        return self.__unique_content_reward

    @property
    def use_on_crew(self) -> bool:
        return self.__use_on_crew

    @property
    def use_on_room(self) -> bool:
        return self.__use_on_room

    @property
    def used_item(self) -> bool:
        return self.__used_item





class ItemDesignMetadata(dict):
    def __init__(self, metadata: str):
        metadata = metadata.strip()
        self.__metadata: _Dict[str, _Any] = _json.loads(metadata) if metadata else {}
        self.__background_sprite_id: int = _parse.int(self.__metadata.get('BackgroundSpriteId'))
        self.__destroyed_sprite_id: int = _parse.int(self.__metadata.get('DestroyedSpriteId'))
        self.__idle_animation_id: int = _parse.int(self.__metadata.get('IdleAnimationId'))
        self.__show_popup_only: int = _parse.bool(self.__metadata.get('ShowPopupOnly'))


    @property
    def background_sprite_id(self) -> int:
        return self.__background_sprite_id

    @property
    def destroyed_sprite_id(self) -> int:
        return self.__destroyed_sprite_id

    @property
    def idle_animation_id(self) -> int:
        return self.__idle_animation_id

    @property
    def metadata(self) -> _Dict[str, _Any]:
        return dict(self.__metadata)

    @property
    def show_popup_only(self) -> bool:
        return self.__show_popup_only