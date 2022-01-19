import functools as _functools
from typing import Any as _Any
from typing import Callable as _Callable
from typing import Dict as _Dict

import pssapi.client as _client
import pssapi.entities as _entities
import pssapi.enums as _enums


class ServiceBase(object):
    def __init__(self, client: _client.PssApiClient) -> None:
        if not client:
            raise ValueError("The parameter 'client' must not be None.")
        self.__client = client

    @property
    def client(self) -> _client.PssApiClient:
        return self.__client

    @property
    def language_key(self) -> _enums.LanguageKey:
        return self.client.language_key

    async def get_latest_version(self) -> "_entities.Setting":
        return await self.client.get_latest_version()

    async def get_production_server(self) -> str:
        return await self.client.get_production_server()


class CacheableServiceBase(ServiceBase):
    def __init__(self, client: _client.PssApiClient, enable_endpoint_cache: bool = True) -> None:
        super().__init__(client)
        self._SERVICE_CACHE: _Dict[str, _Dict[int, _Any]] = {}
        self._enable_endpoint_cache: bool = enable_endpoint_cache or False


def cache_endpoint(version_property_name: str):
    def decorator_endpoint_cache(func: _Callable):
        @_functools.wraps(func)
        async def wrapper_endpoint_cache(self, *args, **kwargs):
            if isinstance(self, CacheableServiceBase) and self._enable_endpoint_cache:
                endpoint_name = func.__name__
                service_cache = self._SERVICE_CACHE
                latest_version = await self.get_latest_version()
                endpoint_data_version = latest_version[version_property_name]

                endpoint_cache = service_cache.get(endpoint_name, {})
                data = endpoint_cache.get(endpoint_data_version)

                if not data:
                    data = await func(self, *args, **kwargs)
                    if endpoint_cache:
                        service_cache[endpoint_name] = {}
                    service_cache.setdefault(endpoint_name, {})[endpoint_data_version] = data
                if isinstance(data, list):
                    return list(data)
                if isinstance(data, dict):
                    return dict(data)
                return data
            else:
                return await func(*args, **kwargs)

        return wrapper_endpoint_cache

    return decorator_endpoint_cache
