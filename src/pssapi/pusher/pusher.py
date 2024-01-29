from inspect import isawaitable
from json import dumps, loads
from platform import system
from typing import Any, Optional

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from websockets.client import connect

import pssapi
from pssapi.constants import PUSHER_APP_CLUSTER, PUSHER_APP_ID
from pssapi.exc import PusherConnectionClosed
from pssapi.pusher.channel import Channel


# TODO: Add error handling, add ping/pong timeout
class Pusher:
    # Should be of the form `platform-library`
    client: str = f"{system()}-pssapi"

    # Pusher protocol (as of 6/1/23, protocol 7)
    protocol: int = 7

    # Time values
    connection_timeout: int = 305
    ping_interval: int = 120

    _socket_id = ""

    _connection = None
    _scheduler = AsyncIOScheduler()

    _channels: dict[Channel] = dict()

    @classmethod
    async def _connect_to_pusher(cls) -> None:
        host = f"ws://ws-{PUSHER_APP_CLUSTER}.pusher.com"
        url = f"{host}/app/{PUSHER_APP_ID}?client={cls.client}&version={pssapi.__version__}&protocol={cls.protocol}"

        cls._connection = await connect(url)
        await cls._send_ping()

    @classmethod
    async def _send_event(cls, event_name: str, data: Any, channel: Optional[str] = None) -> None:
        event = {"event": event_name, "data": data}
        if channel:
            event["channel"] = channel

        event = dumps(event)
        await cls._connection.send(event)

    # Ping pong
    @classmethod
    async def _send_ping(cls) -> None:
        await cls._send_event("pusher:ping", "")

    @classmethod
    async def _send_pong(cls) -> None:
        await cls._send_event("pusher:pong", "")

    @classmethod
    def _reset_connection_timeout(cls, job_id: Any) -> None:
        cls._scheduler.reschedule_job(job_id, trigger=IntervalTrigger(seconds=cls.connection_timeout))

    @classmethod
    async def _connection_closed(cls, code: Optional[int] = None, error_message: Optional[str] = "") -> None:
        await cls._connection.close()

        if code or error_message:
            raise PusherConnectionClosed(
                f"""Connection closed.
Code: {code}
Message: {error_message}""",
                code,
                error_message,
            )

        raise PusherConnectionClosed("Connection timed out / closed with unknown cause.")

    # Scheduled tasks
    @classmethod
    def _start_timers(cls) -> None:
        job_id = cls._scheduler.add_job(cls._connection_closed, IntervalTrigger(seconds=cls.connection_timeout)).id
        cls._scheduler.add_job(cls._send_ping, IntervalTrigger(seconds=cls.ping_interval))

        return job_id

    @classmethod
    async def _subscribe(cls, channel: Channel, token: Optional[str] = "") -> None:
        if channel.private and not token:
            raise ValueError("Token required if channel is private.")

        data = {"channel": channel.name, "auth": await channel._auth(token, cls._socket_id) if channel.private else "", "channel_data": "{}"}
        await cls._send_event("pusher:subscribe", data)

    @classmethod
    def add(cls, channel: Channel) -> None:
        """
        Add a new channel to subscribe to
        Args:
            - `channel` - The channel to subscribe to
        """
        cls._channels[channel.name] = channel

    @classmethod
    async def _handle_message(cls, event: str, data: dict, channel: Optional[str] = "", token: Optional[str] = "") -> None:
        if event == "pusher:connection_established":
            cls._socket_id = data["socket_id"]

            for channel_name in cls._channels.keys():
                channel = cls._channels[channel_name]

                await cls._subscribe(channel, token)

        if event == "pusher:error":
            return await cls._connection_closed(data["code"], data["message"])

        if channel and event == "message":
            channel_class = cls._channels.get(channel)
            if not channel_class:
                return

            callback = channel_class.callback
            if isawaitable(callback):
                return await callback(data)

            return callback(data)

    @classmethod
    def _keep_persistent_connection(cls, token: str, user_id: int) -> None:
        if not token and not user_id:
            return

        if token and not user_id:
            raise RuntimeError("Token specified but not user_id")

        if user_id and not token:
            raise RuntimeError("user_id specified but no token")

        channel = Channel(f"private-user-{user_id}", private=True)
        cls.add(channel)

    @classmethod
    async def run(cls, token: Optional[str] = "", user_id: Optional[int] = 0) -> None:
        """
        Start the Pusher client
        Args:
            - `token`: Account-binded token (required to auth/keep persistent connection)
            - `user_id`: User ID of the account (acquired through `SearchUsers`)
        """
        job_id = cls._start_timers()
        cls._scheduler.start()

        await cls._connect_to_pusher()
        cls._keep_persistent_connection(token, user_id)

        while True:
            message = await cls._connection.recv()
            message = loads(message)
            cls._reset_connection_timeout(job_id)

            event = message["event"]
            data = loads(message["data"]) if isinstance(message["data"], str) else message["data"]
            channel = message["channel"] if message.get("channel") else ""

            await cls._handle_message(event, data, channel, token)
