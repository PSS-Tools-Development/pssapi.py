from asyncio import get_event_loop

from pssapi.enums import PusherChannelType
from pssapi.pusher import Channel, Pusher


async def pusher_example():
    pusher = Pusher

    # Listen to the market channel
    market_channel = Channel(PusherChannelType.MARKET)
    market_channel.on_message(lambda data: print(f"New data: {data}"))
    pusher.add(market_channel)

    # Start listening
    # For persistent connections/private channels:
    # Needs a token (token authorized with UserEmailPasswordAuthorize2), and the user ID of that account
    pusher.run("token", "user_id here")


loop = get_event_loop()
loop.run_until_complete(pusher_example())
