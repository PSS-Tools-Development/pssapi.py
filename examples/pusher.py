from asyncio import get_event_loop

from pssapi.pusher import Pusher
from pssapi.pusher import Channel
from pssapi.enums import PusherChannelType


async def pusher_example():
    pusher = Pusher

    # Listen to the market channel
    market_channel = Channel(PusherChannelType.MARKET)
    market_channel.on_message(lambda data: print(f"New data: {data}"))
    pusher.add(market_channel)

    # For some reason, it is required to listen to the USER_ID_PRIVATE channel to keep the connection persistent
    # Needs to have the same user ID as the ID of the user token
    _ = Channel(f"{PusherChannelType.INCOMING_MESSAGES_PRIVATE}-yourIDhere", private=True)
    _.on_message(lambda __: None)
    pusher.add(_)

    # Start listening
    # Needs a token (token authorized with UserEmailPasswordAuthorize2)
    pusher.run("token")


loop = get_event_loop()
loop.run_until_complete(pusher_example())
