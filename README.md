# jwcook's tilde.team page
Markdown-based static site generated with [Sphinx](docs.readthedocs.io) and [MyST](https://myst-parser.readthedocs.io).

## Usage
Prerequisites:
* python 3.8+

To build:
```bash
pip install -U -r requirements.txt
make docs
```

Or build with live reload:
```bash
make livedocs
```

Publish to tilde.team:
```bash
make publish
```