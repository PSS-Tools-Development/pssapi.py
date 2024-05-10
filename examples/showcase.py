import asyncio
import random

from pssapi import PssApiClient, entities, enums


async def main() -> None:
    client = PssApiClient()
    print(f"Production server: {client.production_server or (await client.get_production_server())}")

    ship_designs: list[entities.ShipDesign] = await client.ship_service.list_all_ship_designs()
    print(f"Found {len(ship_designs)} ship designs.")
    print(f"First ship: {ship_designs[0].ship_design_name}")

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

    room_designs: list[entities.RoomDesign] = await client.room_service.list_room_designs()
    print(f"Found {len(room_designs)} room designs.")
    print(f"First room design: {room_designs[0].room_name}")

    shield_room_designs = [room_design for room_design in room_designs if room_design.room_type_enum == enums.RoomType.SHIELD]
    print(f"Found {len(shield_room_designs)} shield room designs.")
    random.shuffle(shield_room_designs)
    for room_design in sorted(shield_room_designs[:5], key=lambda x: x.room_name):
        shield_room_properties: entities.properties.ShieldRoomProperties = room_design.get_room_type_properties()
        print(f"{room_design.room_name} - Shield points: {shield_room_properties.shield_hp} - Shield restored on reload: {room_design.room_type_properties.shield_room_properties.restore_on_reload}")

    sales = await client.market_service.list_sales_by_item_design_id(0, 81, "Sold", 10)
    print(f"Found {len(sales)} sales.")
    print(f"First sale: {sales[0].id}")

    users = await client.user_service.search_users("The worst.")
    print(f"Found {len(users)} users.")
    user = users[0]
    print(f"First user: {user.id}, {user.name}, {user.trophy} trophies")
    has_user_type_property = "UserType" in user
    print(f'{user} has property "UserType": {has_user_type_property}' + (f' (value: {user["UserType"]})' if has_user_type_property else ""))
    print(f'{user} has property "XYZ": {"XYZ" in user}')


def run_main_synchronous() -> None:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    run_main_synchronous()
