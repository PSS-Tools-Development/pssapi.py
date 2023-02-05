from ..client_base import PssApiClientBase as _PssApiClientBase
from ..enums import LanguageKey as _LanguageKey


class ServiceBase:
    def __init__(self, client: _PssApiClientBase) -> None:
        if not client:
            raise ValueError('The parameter \'client\' must not be None.')
        self.__client: _PssApiClientBase = client

    @property
    def client(self) -> _PssApiClientBase:
        return self.__client

    @property
    def language_key(self) -> _LanguageKey:
        return self.client.language_key


    async def get_production_server(self) -> str:
        return (await self.client.get_production_server())
