"""Sphinx extension that extends sphinx-design grid-item-card directive with additional options
and defaults
"""

from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx_design.grids import GridItemCardDirective

PROFILE_PIC_DIR = '../assets/images/profile_pics'


class ProfileCardDirective(GridItemCardDirective):
    option_spec = {
        'yt-channel': directives.unchanged,
        'tw-channel': directives.unchanged,
        **GridItemCardDirective.option_spec,
    }

    def run(self):
        """Run the directive."""
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


def setup(app: Sphinx):
    """Setup the grid components."""
    app.add_directive('profile-card', ProfileCardDirective)
