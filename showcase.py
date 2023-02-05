import asyncio

import pssapi
from pssapi.entities import ShipDesign


async def main() -> None:
    client = pssapi.PssApiClient()
    print(f'Production server: {client.production_server or (await client.get_production_server())}')

    ship_designs: list[ShipDesign] = await client.ship_service.list_all_ship_designs()
    print(f'Found {len(ship_designs)} ship designs.')
    print(f'First ship: {ship_designs[0].ship_design_name}')

    item_designs = await client.item_service.list_item_designs()
    print(f'Found {len(item_designs)} item designs.')
    print(f'First item: {item_designs[0].item_design_name}')

    sales = await client.market_service.list_sales_by_item_design_id(0, 81, 'Sold', 10)
    print(f'Found {len(sales)} sales.')
    print(f'First sale: {sales[0].id}')

    users = await client.user_service.search_users('The worst.')
    print(f'Found {len(users)} users.')
    print(f'First user: {users[0].id}, {users[0].name}, {users[0].trophy} trophies')


def run_main_synchronous() -> None:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run_main_synchronous()
