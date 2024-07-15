# Config for Sphinx and its extensions
from pathlib import Path
from shutil import rmtree

from sphinx.application import Sphinx

ROOT_DIR = Path('.').resolve().parent
BUILD_DIR = ROOT_DIR / '_build' / 'html'
PAGES_DIR = ROOT_DIR / 'pages'
TAGS_DIR = PAGES_DIR / 'tags'
BASE_URL = 'https://jwcook.tilde.team'

# General information about the project.
project = '~jwcook'
needs_sphinx = '4.0'
master_doc = 'index'
source_suffix = ['.md', '.rst']
version = release = '0.1.0'
html_static_path = [
    '../assets/css',
    '../assets/js',
]  # Exclude assets/images (automatically copied)
exclude_patterns = ['_build', 'README.md']
templates_path = ['../templates']

# Sphinx extensions
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autosummary',
    'sphinx.ext.extlinks',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinx_sitemap',
    'sphinx_tags',
    'sphinxext.opengraph',
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

# autosectionlabel_prefix_document = True

# Sphinx-tags settings
tags_create_tags = True
tags_create_tag_index = False
tags_create_tag_toctree = False
tags_extension = ['md']
tags_output_dir = 'tags'
tags_overview_title = '{fas}`tags` Tags'
tags_page_title = '{fas}`tag`'
tags_page_header = "Pages with this tag"
tags_create_badges = True
# Reference: https://sphinx-design.readthedocs.io/en/latest/badges_buttons.html
tags_badge_colors = {
    'python': 'primary',
    'code': 'secondary',
    'docs': 'secondary',
    'plants': 'success',
    'nature': 'success',
    'photography': 'warning',
    'status:*': 'info',
    '*': 'dark',
}

# Since we're not on readthedocs, don't insert `/<language>/<version>/`
notfound_urls_prefix = ''

# Sitemap config
html_baseurl = f'{BASE_URL}/'
sitemap_excludes = ['404.html', 'asdf.html', 'genindex.html', 'search.html']
sitemap_url_scheme = '{link}'

# OpenGraph settings
# TODO: custom meta tags
ogp_site_url = BASE_URL
ogp_image = f'{BASE_URL}/_static/avatar.png'
ogp_use_first_image = True
ogp_social_cards = {'font': 'JetBrainsMono'}
ogp_custom_meta_tags = []

# HTML general settings
# html_favicon = join('../assets', 'favicon.ico')
html_css_files = [
    'fonts.css',
    'style.css',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css',
]
html_extra_path = ['robots.txt']
html_js_files = ['style.js']
html_title = '~jwcook'
html_logo = '../assets/images/avatar.png'
html_last_updated_fmt = '%Y-%m-%d'
html_show_copyright = False
html_show_sphinx = False

# HTML theme settings
pygments_style = 'gruvbox-light'
pygments_dark_style = 'gruvbox-dark'
html_theme = 'furo'

# Color variable reference: https://github.com/pradyunsg/furo/blob/main/src/furo/assets/styles/variables/_colors.scss
html_theme_options = {
    # 'light_logo': 'logo-light.webp',
    # 'dark_logo': 'logo-dark.webp',
    'sidebar_hide_name': True,
    'light_css_variables': {
        'font-stack': 'JetBrainsMono',
        'color-brand-primary': '#b57614',
        'color-brand-content': '#076678',
        # 'color-foreground-primary': 'black',
        # 'color-foreground-secondary': '#5a5c63',
        # 'color-foreground-muted': '#646776',
        # 'color-foreground-border': '#878787',
        'color-background-primary': '#d5c4a1',
        'color-background-secondary': '#ebdbb2',
        # 'color-background-hover': '#efeff4ff',
        # 'color-background-hover--transparent': '#efeff400',
        # 'color-background-border': '#eeebee',
        # 'color-background-item': '#ccc',
    },
    'dark_css_variables': {
        'font-stack': 'JetBrainsMono',
        'color-brand-primary': '#fabd2f',
        'color-brand-content': '#83a598',
        # 'color-foreground-primary': '#ffffffcc',  # for main text and headings
        # 'color-foreground-secondary': '#9ca0a5',  # for secondary text
        # 'color-foreground-muted': '#81868d',  # for muted text
        # 'color-foreground-border': '#666666',  # for content borders
        'color-background-primary': '#504945',  # for content
        'color-background-secondary': '#3c3836',  # for navigation + ToC
        # 'color-background-hover': '#1e2124ff',  # for navigation-item hover
        # 'color-background-hover--transparent': '#1e212400',
        # 'color-background-border': '#3c3836',  # for UI borders
        # 'color-background-item': '#444',  # for 'background' items (eg': ' copybutton)
    },
}
# Gruvbox colors:
# bg0 #282828
# bg1 #3c3836
# bg2 #504945
# bg3 #665c54
# bg4 #7c6f64
# gray #928374


SIDEBAR_MAXDEPTH = 2


def setup(app: Sphinx):
    """Run some additional steps after the Sphinx builder is initialized"""
    app.connect('build-finished', combine_static_dirs, priority=1000)
    app.connect('build-finished', rm_txt_sources, priority=1000)


def combine_static_dirs(*args):
    """Move/deduplicate static files from Sphinx extensions"""
    src = BUILD_DIR / '_sphinx_design_static'
    if not src.exists():
        return
    dst = BUILD_DIR / '_static'
    for item in src.iterdir():
        item.rename(dst / item.name)
    src.rmdir()


def rm_txt_sources(*args):
    """Remove _sources dir used by Sphinx for unused 'show source' button"""
    rmtree(BUILD_DIR / '_sources')
