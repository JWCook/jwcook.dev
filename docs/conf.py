from os.path import join
from pathlib import Path
from shutil import copy

# General information about the project.
project = 'jwcook'
needs_sphinx = '4.0'
master_doc = 'index'
source_suffix = ['.md', '.rst']
version = release = '0.0.1'
html_static_path = ['_static']
exclude_patterns = ['_build']
templates_path = ['_templates']

# Sphinx extensions
extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.extlinks',
    'sphinx_design',
    'myst_parser',
    'notfound.extension',
]

# MyST extensions
myst_enable_extensions = [
    'colon_fence',
    'html_image',
    'linkify',
    'replacements',
    'smartquotes',
]

# Strip prompt text when copying code blocks with copy button
copybutton_prompt_text = r'>>> |\.\.\. |\$ '
copybutton_prompt_is_regexp = True

# HTML general settings
# html_favicon = join('_static', 'favicon.ico')
html_css_files = [
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css',
]
html_title = 'jwcook\'s home page'
html_logo = '_static/logo.png'
html_show_copyright = False
html_show_sphinx = False
# notfound_default_version = 'stable'
# pygments_style = 'friendly'
# pygments_dark_style = 'material'

# HTML theme settings
html_theme = 'gruvboxsphinx'
# html_theme = 'furo'
# html_theme_options = {
#     'light_logo': 'requests-cache-logo-light.webp',
#     'dark_logo': 'requests-cache-logo-dark.webp',
#     'sidebar_hide_name': True,
#     'light_css_variables': {
#         'color-brand-primary': '#0288d1',
#         'color-brand-content': '#2a5adf',
#     },
#     'dark_css_variables': {
#         'color-brand-primary': '#5eb8ff',
#         'color-brand-content': '#368ce2',
#     },
# }
