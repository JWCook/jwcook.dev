# jwcook's home page
* Main site: https://jwcook.dev
* Tilde site: https://tilde.team/~jwcook

Markdown-based static site generated with [Sphinx](docs.readthedocs.io) and [MyST](https://myst-parser.readthedocs.io).

## License
* Code located under `/src` is under the [MIT License](LICENSE-SRC)
* All other content is under Creative Commons [CC-BY-NC-SA](LICENSE)

## Setup
Prerequisites:
* python 3.10+
* [`just`](https://github.com/casey/just#packages)
* [`npm`](https://docs.npmjs.com/cli/v10/configuring-npm/install)

Install dependencies:
```bash
pip install -Ue "."
npm install
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

Publish:
```bash
just publish
```
