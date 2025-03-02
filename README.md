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
* [`uv`](https://docs.astral.sh/uv/getting-started/installation)
* [`just`](https://github.com/casey/just#packages)
* [`npm`](https://docs.npmjs.com/cli/v10/configuring-npm/install)

<details>
<summary>Quick install</summary>

```sh
# Install uv, python, and just
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.13
uv tool install rust-just

# Install node, nvm and npm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
source $HOME/.nvm/nvm.sh
nvm install 22
```

</details>

Install dependencies:
```sh
uv sync --frozen
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
