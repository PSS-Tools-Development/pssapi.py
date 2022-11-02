import asyncio

import pssapi
from pssapi.entities import ShipDesign


async def main() -> None:
    client = await pssapi.PssApiClient.create()
    print(f'Production server: {client.production_server}')

    ship_designs: list[ShipDesign] = await client.ship_service.list_all_ship_designs()
    print(f'Found {len(ship_designs)} ship designs.')
    print(f'First ship: {ship_designs[0].ship_design_name}')

    item_designs = await client.item_service.list_item_designs()
    print(f'Found {len(item_designs)} item designs.')


def run_main_synchronous() -> None:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run_main_synchronous()
