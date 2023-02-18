import pssapi.client as _client
import pssapi.enums as _enums


class ServiceBase:
    def __init__(self, client: _client.PssApiClient) -> None:
        if not client:
            raise ValueError('The parameter \'client\' must not be None.')
        self.__client = client

    @property
    def client(self) -> _client.PssApiClient:
        return self.__client

    @property
    def language_key(self) -> _enums.LanguageKey:
        return self.client.language_key

    async def get_production_server(self) -> str:
        return (await self.client.get_production_server())
