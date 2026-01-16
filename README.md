# Unicode to RTF command code conversion

[![PyPI version](https://img.shields.io/pypi/v/rtfunicode.svg)](https://pypi.python.org/project/rtfunicode)
[![License](https://img.shields.io/pypi/l/rtfunicode.svg)](https://github.com/mjpieters/rtfunicode/blob/main/LICENSE.txt)
![Python versions supported](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fmjpieters%2Frtfunicode%2Fmain%2Fpyproject.toml)
[![Built with uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Checked with Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with Pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/)
[![Python checks](https://github.com/mjpieters/rtfunicode/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/mjpieters/rtfunicode/actions/workflows/ci-cd.yml)
[![Coverage](https://codecov.io/gh/mjpieters/rtfunicode/graph/badge.svg?token=ZRZO4XRBP6)](https://codecov.io/gh/mjpieters/rtfunicode)

This module implements an encoder for unicode to RTF 1.5 command sequences; it
can be used to generate valid RTF output with international characters.

Importing this module adds a new `rtfunicode` codec, allowing you to encode
unicode strings to valid RTF bytecode sequences:

```pycon
>>> import rtfunicode
>>> 'RTF and unicode mix just fine! \u263A'.encode('rtfunicode')
'RTF and unicode mix just fine! \\u9786?'
```

The RTF command code for a unicode character is `\uN?`, where N is a signed
16-bit integer and the ? is a placeholder character for older RTF readers. This
module sets the latter to the '?' literal for simplicity's sake.

## Requirements

* Python 3.10 or newer.


## Development

The project code is hosted on [GitHub][], feel free to report issues,
fork the code and issue pull requests.

[GitHub]: https://github.com/mjpieters/rtfunicode

This project uses [`uv`](https://docs.astral.sh/uv/) to handle Python dependencies and environments; use `uv sync` to get an up-to-date virtualenv with all dependencies. This includes development dependencies such as [Ruff](https://docs.astral.sh/ruff/) (used for linting and formatting) and [Pyright](https://microsoft.github.io/pyright/) (used to validate type annotations).

### Linting and formatting

While PRs and commits on GitHub are checked for linting and formatting issues, it's easier to check for issues locally first. After running `uv sync`, run `uv run pre-commit install` to install [pre-commit](https://pre-commit.com/) hooks that will run these tools and format your changes automatically on commits. These hooks also run `uv sync` whenever your working tree changes.

### Testing

This project uses `pytest` to run its tests: `uv run pytest`.

## License

BSD 2-Clause (simplified), see: [LICENSE.txt](./LICENSE.txt)


## Author

Martijn Pieters <mj@zopatista.com>
