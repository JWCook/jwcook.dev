"""
Tiny sphinx extension that formats HTML output. Requires `tidy` to be installed.
Reference:
* https://countergram.github.io/pytidylib
* https://www.html-tidy.org/documentation
* https://api.html-tidy.org/tidy/quickref_5.8.0.html

Note: tidying adds about 10-20% to HTML file size.

Config example in `conf.py`:
```python
extensions = ['sphinx-tidy']
tidy_options = {'wrap': 80}
```
"""

from logging import getLogger

import sphinx
from tidylib.tidy import BASE_OPTIONS, tidy_document

TIDY_OPTIONS = {
    'drop-empty-elements': False,
    **BASE_OPTIONS,
}
logger = getLogger(__name__)


def setup(app: sphinx):
    app.add_config_value('tidy_options', {}, 'html')
    app.connect('build-finished', tidy_html)


def tidy_html(app, exception):
    """Tidy all HTML files in the output directory"""
    for html_file in app.outdir.rglob('*.html'):
        logger.debug(f'Tidying {html_file}')
        html = html_file.read_text()
        html, errors = tidy_document(html, options=_merge_options(app))
        logger.debug(f'Tidy errors: {errors}')
        with html_file.open('w') as f:
            f.write(html)


def _merge_options(app) -> dict:
    """Merge default and user-defined options. Allow `True`/`False` values instead of 1/0."""
    options = {**TIDY_OPTIONS, **app.config.tidy_options}
    for k, v in options.items():
        if v is True:
            options[k] = 1
        elif v is False:
            options[k] = 0
    logger.debug(f'Tidying with options: {options}')
    return options
