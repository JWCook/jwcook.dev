from os.path import join
from pathlib import Path
from shutil import copy

# General information about the project.
project = 'jwcook'
needs_sphinx = '4.0'
master_doc = 'index'
source_suffix = ['.md', '.rst']
version = release = '0.0.1'
html_static_path = ['../assets']
exclude_patterns = ['_build', 'README.md']
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

# HTML general settings
# html_favicon = join('../assets', 'favicon.ico')
html_css_files = [
    'fonts.css',
    'style.css',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css',
]
html_title = 'jwcook\'s home page'
# html_logo = '../assets/logo.png'
html_show_copyright = False
html_show_sphinx = False

# HTML theme settings
pygments_style = 'gruvbox-light'
pygments_dark_style = 'gruvbox-dark'
html_theme = 'furo'
html_theme_options = {
    # 'light_logo': 'logo-light.webp',
    # 'dark_logo': 'logo-dark.webp',
    'sidebar_hide_name': True,
    'light_css_variables': {
        'font-stack': 'JetBrainsMono',
        'color-brand-primary': '#b57614',
        'color-brand-content': '#076678',
    },
    'dark_css_variables': {
        'font-stack': 'JetBrainsMono',
        'color-brand-primary': '#fabd2f',
        'color-brand-content': '#83a598',
    },
}
