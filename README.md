# pssapi.py

<a href="https://discord.gg/kKguSec" target="_blank"><img src="https://discord.com/api/guilds/565819215731228672/embed.png" alt="Support Discord server invite"></a>
<a href="https://pypi.org/project/pssapi" target="_blank"><img src="https://img.shields.io/pypi/status/pssapi?color=%23DAB420&label=status" alt="Development status"></a>
<a href="https://pypi.org/project/pssapi" target="_blank"><img src="https://img.shields.io/pypi/v/pssapi?color=%23DAB420&label=pypi%20package" alt="Package version"></a>
<a href="https://pypi.org/project/pssapi" target="_blank"><img src="https://img.shields.io/pypi/pyversions/pssapi.svg?color=%23DAB420" alt="Supported Python versions"></a>
<img src="https://img.shields.io/codecov/c/github/pss-tools-development/pssapi.py" alt="Code coverage">

> An async client library to access the [Pixel Starships API](https://pixelstarships.com).

# ✨ Features
- **Fully typehinted** so your favorite IDE can assist you with code completion.
- **Easy access** to any instance of a **Pixel Starships API** server.
- **Fast setup** to get you started quickly.
- **Caching versioned endpoints** to cut down traffic between your app and the servers.

# 🔍 Future plans

- Use and support [pydantic](https://docs.pydantic.dev/latest/) models
- Implement aliases and properties to map values displayed in-game to the raw values returned by the API

# 🚀 Demo
To retrieve a list of all item designs:
```python
import asyncio
from pssapi import PssApiClient

async def main():
    client = PssApiClient()

    item_designs = await client.item_service.list_item_designs()
    print(f"Found {len(item_designs)} item designs.")
    print(f"First item: {item_designs[0].item_design_name}")

if __name__ == "__main__":
    asyncio.run(main())
```

## ⚙️ Installation
**Python 3.11 or higher is required**

To install the latest version of this library, run the following command:
```sh
pip install -U pssapi
```

# 🖊️ Contribute
If you ran across a bug or have a feature request, please check if there's [already an issue](https://github.com/PSS-Tools-Development/pssapi.py/issues) for that and if not, [open a new one](https://github.com/PSS-Tools-Development/pssapi.py/issues/new).

If you want to fix a bug or add a feature, please check out the [Contribution Guide](CONTRIBUTING.md).

# 🆘 Support
If you need help using the library or want to contribute, you can join the support Discord at: [discord.gg/kKguSec](https://discord.gg/kKguSec)

# 👥 Contributors

- [The worst.](https://github.com/Zukunftsmusik)
- [Solevis](https://github.com/solevis)
- [architelos](https://github.com/architelos)

# 🔗 Links
- Documentation (tbd)
- [Official Support Discord server](https://discord.gg/kKguSec)
- [Pixel Starships homepage](https://pixelstarships.com)
- [Official Pixel Starships Discord](https://discord.gg/pss) (not affiliated to this library)
