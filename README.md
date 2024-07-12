# jwcook's tilde.team page
https://tilde.team/~jwcook

Markdown-based static site generated with [Sphinx](docs.readthedocs.io) and [MyST](https://myst-parser.readthedocs.io).

## Setup
Prerequisites:
* python 3.10+
* [`just`](https://github.com/casey/just#packages)
* Install dependencies:
```bash
pip install -Ue "."
```

## Usage
Build:
```bash
just build
```

Build with live browser reload:
```bash
just live
```

Publish to tilde.team:
```bash
just publish
```
