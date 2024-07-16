"""
Tiny sphinx extension that formats HTML output. Requires tidy to be installed.
Reference:
* https://countergram.github.io/pytidylib
* https://www.html-tidy.org/documentation
* https://api.html-tidy.org/tidy/quickref_5.8.0.html

Config example:
```python
# conf.py
extensions = ['sphinx-tidy']
tidy_options = {'wrap': True}
```
"""
from logging import getLogger

from sphinx.application import Sphinx
from tidylib.tidy import BASE_OPTIONS, tidy_document

TIDY_OPTIONS = {
    'output-xhtml': 1,
    'show-body-only': 1,
    'drop-empty-elements': 0,
    **BASE_OPTIONS,
}
logger = getLogger(__name__)


def setup(app: Sphinx):
    app.add_config_value('tidy_options', {}, 'html')
    app.connect('html-page-context', tidy_html)


def tidy_html(app, pagename, templatename, context, doctree):
    if html := context.get('body'):
        html, errors = tidy_document(html, options=_merge_options(app))
        if errors:
            logger.warning('Tidy errors: %s', errors)
        context['body'] = html


def _merge_options(app) -> dict:
    """Merge default and user-defined options. Allow `True`/`False` values instead of 1/0."""
    options = {**TIDY_OPTIONS, **app.config.tidy_options}
    for k, v in options.items():
        if v is True:
            options[k] = 1
        elif v is False:
            options[k] = 0
    logger.debug('Tidying with options: %s', options)
    return options
