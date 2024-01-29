from json import loads
from typing import Callable, Optional

from aiohttp import ClientSession

from pssapi.constants import PUSHER_AUTH_URL


class Channel:
    def __init__(self, name: str, private: Optional[bool] = False, endpoint: Optional[str] = PUSHER_AUTH_URL) -> None:
        """
        Create a new `Channel` instance

        Args:
            `name` - Name of the channel
            `endpoint` - Authentication endpoint
            `private` - Whether the channel is private (requires `token` to be specified)
        """
        self.name = name
        self.endpoint = endpoint
        self.private = private
        self.callback = lambda _: None

    def on_message(self, callback: Optional[Callable]) -> None:
        """
        Set a callback to be called when a message is received

        Args:
            `callback` - The function to be called, `lambda _: None` if not specified
        """
        if callback:
            self.callback = callback

        else:
            self.callback = lambda _: None

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
