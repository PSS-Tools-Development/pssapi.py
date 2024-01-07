from json import loads
from typing import Callable, Optional

from aiohttp import ClientSession

from pssapi.constants import PUSHER_AUTH_URL


class Channel:
    def __init__(self, name: str, private: Optional[bool] = False, endpoint: Optional[str] = PUSHER_AUTH_URL) -> None:
        self.name = name
        self.endpoint = endpoint
        self.private = private
        self.callback = lambda _: None

    def on_message(self, callback: Callable) -> None:
        self.callback = callback

    async def _auth(self, token: str, socket_id: str) -> str:
        data = {
            "channel_name": self.name,
            "socket_id": socket_id,
        }
        endpoint = f"{self.endpoint}?accessToken={token}"

        async with ClientSession() as session:
            async with session.post(endpoint, data=data) as response:
                assert response.ok, "Couldn't authenticate connection"

                return loads(await response.text())["auth"]
