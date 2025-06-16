import asyncio
import os
from xml.etree import ElementTree

from pssapi import PssApiClient, entities


async def main() -> None:
    # Create a client with default settings
    # The production server can be passed into the constructor, e.g. if you want to access the test servers
    # If you don't pass a production server, the client will automatically determine it before making any API request
    client = PssApiClient()
    print(f"Production server: {client.production_server or (await client.get_production_server())}")

    # Get some data not requiring authentication and authorization
    ship_designs: list[entities.ShipDesign] = await client.ship_service.list_all_ship_designs()
    print(f"Found {len(ship_designs)} ship designs.")
    print(f"First ship: {ship_designs[0].ship_design_name}")

    character_designs: list[entities.CharacterDesign] = await client.character_service.list_all_character_designs()
    print(f"Found {len(character_designs)} character designs.")
    print(f"First character: {character_designs[0].character_design_name}")
    xml = ElementTree.tostring(character_designs[0].node).decode().replace("\n", " ")
    print(f"First character XML: {xml}")

    item_designs: list[entities.ItemDesign] = await client.item_service.list_item_designs()
    print(f"Found {len(item_designs)} item designs.")
    print(f"First item: {item_designs[0].item_design_name}")

    item_designs_cached: list[entities.ItemDesign] = await client.item_service.list_item_designs()
    print(f"Found {len(item_designs_cached)} cached item designs.")
    print(f"First cached item: {item_designs_cached[0].item_design_name}")

    if item_designs[0] == item_designs_cached[0]:
        print("Item with index 0 equals cached item with index 0")

    if item_designs[0] != item_designs_cached[1]:
        print("Item with index 0 not equals to cached item with index 1")

    sales = await client.market_service.list_sales_by_item_design_id(0, 81, "Sold", 10)
    print(f"Found {len(sales)} sales.")
    print(f"First sale: {sales[0].id}")

    users = await client.user_service.search_users("The worst.")
    print(f"Found {len(users)} users.")
    user = users[0]
    print(f"First user: {user.id}, {user.name}, {user.trophy} trophies")
    has_highest_user_type_property = "UserType" in user
    print(f'{user} has property "UserType": {has_highest_user_type_property}' + (f' (value: {user["UserType"]})' if has_highest_user_type_property else ""))
    print(f'{user} has property "XYZ": {"XYZ" in user}')

    # Do a simple device login to get an access token,
    # A device key is required, here we use one that was generated using str(uuid.uuid4())
    # Make sure to not generate a new device key on each login or you can only log in 5 times within 24 hours.
    device_key = "bdf1c128-1e7e-4a17-8e6e-98fd89e28f68"

    # A secret "checksum key" is also required, without the checksum_key a login is not possible.
    checksum_key = os.environ.get("PSS_DEVICE_LOGIN_CHECKSUM_KEY")

    if checksum_key:
        # Do the login using the latest supported login endpoint
        user_login = await client.device_login(device_key, checksum_key)

        # Grab the access token
        access_token = user_login.access_token

        # Use the access token to search for an alliance (a fleet), limit the number of results to 30
        alliances = await client.alliance_service.search_alliances(access_token, "Game", 0, 30)
        print(f"Found {len(alliances)} fleets.")
        fleets_named_game_of_phones = [alliance for alliance in alliances if alliance.alliance_name.lower() == "game of phones"]
        if fleets_named_game_of_phones:
            game_of_phones = fleets_named_game_of_phones[0]
            print(f"Fleet '{game_of_phones.alliance_name}' (ID: {game_of_phones.id}) has {game_of_phones.number_of_members} members.")
        else:
            print("A fleet with the name 'game of phones' could not be found.")


def run_main_synchronous() -> None:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    run_main_synchronous()
