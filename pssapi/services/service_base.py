

class PssServiceBase():
    def __init__(self, production_server: str) -> None:
        self.__production_server: str = production_server


    @property
    def production_server(self) -> str:
        return self.__production_server