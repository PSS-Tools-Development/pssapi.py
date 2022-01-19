import asyncio

from pssapi import PssApiClient
from pssapi.entities import ShipDesign


async def main() -> None:
    client = PssApiClient()
    print(f"Production server: {client.production_server or (await client.get_production_server())}")

    ship_designs: list[ShipDesign] = await client.ship_service.list_all_ship_designs()
    print(f"Found {len(ship_designs)} ship designs.")
    print(f"First ship: {ship_designs[0].ship_design_name}")

    item_designs = await client.item_service.list_item_designs()
    print(f"Found {len(item_designs)} item designs.")
    print(f"First item: {item_designs[0].item_design_name}")

    item_designs_cached = await client.item_service.list_item_designs()
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


def run_main_synchronous() -> None:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    run_main_synchronous()
