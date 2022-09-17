from ..enums import LanguageKey as _LanguageKey


class PssServiceBase:
    def __init__(self, production_server: str, language_key: _LanguageKey) -> None:
        self.__language_key: _LanguageKey = language_key
        self.__production_server: str = production_server

    @property
    def language_key(self) -> _LanguageKey:
        return self.__language_key

    @property
    def production_server(self) -> str:
        return self.__production_server
