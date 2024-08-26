# pssapi.py - Contribution Guide
If you want to fix a bug or add a new feature, [fork the repository](https://github.com/PSS-Tools-Development/pssapi.py/fork) to your own github account, make the changes and [open a pull request](https://github.com/PSS-Tools-Development/pssapi.py/compare). Make sure to add tests for your changes and run all tests before opening the pull request.

# Setup your development environment
This project makes use of [uv](https://github.com/astral-sh/uv) for package dependency management and [Make](https://www.gnu.org/software/make/) for some CLI command shortcuts. If you're developing on Windows, it's recommended to install [Windows Subsystem for Linux (WSL 2)](https://learn.microsoft.com/en-us/windows/wsl/install).

An installation of Python is not required, **uv** will handle this.

## Windows
- Install [chocolatey](https://chocolatey.org/install) (a package manager).
- Run `choco install make` to install **Make**.
- Follow the [installation instructions](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) of **uv**.

## Linux / Windows Subsystem for Linux (WSL 2)
- Run `sudo apt-get update && sudo apt-get install make` to install **Make**.
- Follow the [installation instructions](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) of **uv**.

## Subsequent steps
- Open a terminal
- Clone the forked repository onto your machine, e.g. into the folder `~/development/`
- Navigate to the workspace folder, e.g. to `~/development/pssapi.py`
- Run `make init-dev`. This command will:
  - Update **uv** to the latest version
  - Create a virtual environment in the workspace folder and install all dependencies
  - Install pre-commit hooks that will ensure proper code formatting before committing your changes
  - Run the new pre-commit hooks

# 🥳 Now you're all set up to start coding! 🎉

# Publishing the package to PyPi.org (from Linux)

1. Create a [.pypirc](https://packaging.python.org/en/latest/specifications/pypirc/) file in your home directory: `~/.pypirc`
2. Open the file and write the following into it:
```ini
[distutils]
index-servers =
	pssapi.py

[pssapi.py]
repository = https://upload.pypi.org/legacy/
username = __token__
password = <YOUR PROJECT-SPECIFIC TOKEN>
```
3. Go to [The pssapi.py management page](https://pypi.org/manage/project/pssapi/settings/) and create an API Token
4. Replace `<YOUR PROJECT-SPECIFIC TOKEN>` in step 2 with the token you've just generated
5. Use `make publish` to publish the package to pypi.org. The command will:
   - Clean the build directory
   - Build the package
   - Check the distribution files
   - Publish the package
