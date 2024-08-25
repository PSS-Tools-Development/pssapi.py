from asyncio import new_event_loop, set_event_loop
from typing import Dict

import pssapi


MARKET_DATA: Dict[int, pssapi.entities.Message] = {}
TOKEN: str = ""
USER_ID: str = ""


async def pusher_example():
    pusher = pssapi.pusher.Pusher

    # Listen to the market channel
    market_channel = pssapi.pusher.Channel(pssapi.enums.PusherChannelType.MARKET)
    market_channel.on_message(process_market_data)
    pusher.add(market_channel)

    # Start listening
    # For persistent connections/private channels:
    # Needs a token (token authorized with UserEmailPasswordAuthorize2), and the user ID of that account
    await pusher.run(TOKEN, USER_ID)


def process_market_data(data: Dict):
    message = pssapi.entities.Message(data)
    MARKET_DATA[message.sale_id] = message
    if message.activity_type == pssapi.enums.ActivityType.MARKET_LISTED:
        print(f"{message.user_name} {message.message} for {message.activity_argument} (Sale ID: {message.sale_id})")
    elif message.activity_type == pssapi.enums.ActivityType.MARKET_SOLD:
        if message.sale_id in MARKET_DATA:
            print(f"Sale {message.sale_id} completed ({message.user_name} {MARKET_DATA[message.sale_id].message} for {message.activity_argument})")
        else:
            print(f"Sale {message.sale_id} completed")
    else:
        print(f"New data: {message}")
    print(dict(message))


if __name__ == "__main__":
    loop = new_event_loop()
    set_event_loop(loop)

    loop.run_until_complete(pusher_example())
