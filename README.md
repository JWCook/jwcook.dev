# jwcook's tilde.team page
https://tilde.team/~jwcook

Markdown-based static site generated with [Sphinx](docs.readthedocs.io) and [MyST](https://myst-parser.readthedocs.io).

## Setup
Prerequisites:
* python 3.8+

```bash
pip install -U -r requirements.txt
```

## Usage
Build:
```bash
make docs
```

Build with live reload:
```bash
make livedocs
```

Publish to tilde.team:
```bash
make publish
```