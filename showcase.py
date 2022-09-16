import asyncio as _asyncio

import pssapi


async def main() -> None:
    client = pssapi.PssApiClient(production_server='api2.pixelstarships.com')
    print(f'Production server: {client.production_server}')

    item_designs = await client.item_service.list_item_designs_2()
    print(f'Found {len(item_designs)} item designs.')


def run_main_synchronous() -> None:
    loop = _asyncio.get_event_loop()
    loop.run_until_complete(main())


if __name__ == '__main__':
    run_main_synchronous()