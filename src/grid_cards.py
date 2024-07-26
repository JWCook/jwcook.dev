"""Sphinx extension that extends sphinx-design grid-item-card directive with additional options
and defaults
"""

from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx_design.grids import GridItemCardDirective

from . import ROOT_DIR
from .dl_favicons import download_favicon

PROFILE_PIC_DIR = '../assets/images/profile_pics'
DEFAULT_FAVICON = '../assets/images/favicons/default_favicon.png'


class ProfileCardDirective(GridItemCardDirective):
    """Card item with a 128px profile pic"""

    option_spec = {
        'yt-channel': directives.unchanged,
        'tw-channel': directives.unchanged,
        **GridItemCardDirective.option_spec,
    }

    def run(self):
        self.options.setdefault('class-img-top', ['md-profile'])
        self.options.setdefault('class-title', ['md-secondary'])
        if yt_channel := self.options.get('yt-channel'):
            self.options.setdefault('link', f'https://youtube.com/@{yt_channel}')
            self.options.setdefault('img-top', f'{PROFILE_PIC_DIR}/{yt_channel.lower()}.png')
            self.options.pop('yt-channel')
        if tw_channel := self.options.get('tw-channel'):
            self.options.setdefault('link', f'https://twitch.tv/{tw_channel}')
            self.options.setdefault('img-top', f'{PROFILE_PIC_DIR}/{tw_channel.lower()}.png')
            self.options.pop('tw-channel')
        return super().run()


class FaviconCardDirective(GridItemCardDirective):
    """Card item with a 40px favicon"""

    def run(self):
        self.options.setdefault('class-img-top', ['md-favicon'])
        self.options.setdefault('class-title', ['md-secondary'])
        if url := self.options.get('link'):
            # Download favicon, and add path relative to pages dir
            if favicon_path := download_favicon(url):
                favicon_path = f'../{favicon_path.relative_to(ROOT_DIR)}'
            else:
                favicon_path = DEFAULT_FAVICON
            self.options.setdefault('img-top', favicon_path)
        return super().run()


def setup(app: Sphinx):
    app.add_directive('profile-card', ProfileCardDirective)
    app.add_directive('favicon-card', FaviconCardDirective)
