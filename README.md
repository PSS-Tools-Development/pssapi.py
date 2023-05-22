# Wrapper for the Pixel Starships API

This library allows you to request the Pixel Starships API through a Python Wrapper.

## Supported Platforms

- Python: 3.11

## Usage

### Installation

You can install this module using your package management method. For example:

```bash
pip install pssapi
```

### Get started

```python
import asyncio

from pssapi import PssApiClient


async def main():
    client = PssApiClient()

    item_designs = await client.item_service.list_item_designs()
    print(f"Found {len(item_designs)} item designs.")
    print(f"First item: {item_designs[0].item_design_name}")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.run(main())
```

## Contributing

### Install development dependencies
Linux:

```bash
make init
```

Windows:

```bash
./win init
```

### Format code
Linux:

```bash
make format
```

Windows:
```bash
./win format
```

### Check & Test
Linux:

```bash
make check
make test
```

Windows:
```bash
./win check
./win test
```

### Showcase

```bash
poetry run python examples/showcase.py
```
