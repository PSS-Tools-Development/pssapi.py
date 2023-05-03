# Wrapper for the Pixel Starships API

## Usage

### Installation

```bash
pip install -e git+ssh://git@github.com/PSS-Tools-Development/pssapi.py.git@v0.1.0#egg=pssapi
```

### Example

```python
import asyncio

from pssapi import PssApiClient
from pssapi.entities import ShipDesign


async def main() -> None:
    client = PssApiClient()
    print(f"Production server: {client.production_server or (await client.get_production_server())}")

    item_designs = await client.item_service.list_item_designs()
    print(f"Found {len(item_designs)} item designs.")
    print(f"First item: {item_designs[0].item_design_name}")


def run_main_synchronous() -> None:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    run_main_synchronous()
```

## Contributing

### Install development dependencies

```bash
make init
```

### Format code

```bash
make format
```

### Check & Test

```bash
make check
make test
```

### Showcase

```bash
# install locally pssapi.py
pip install -e .

# run the showcase with examples
python showcase.py
```
