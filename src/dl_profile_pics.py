#!/usr/bin/env python
"""Script to download YouTube profile pics.
This allows serving smaller compressed images along with the site, to limit external requests.
"""

import re
from logging import getLogger
from pathlib import Path

from bs4 import BeautifulSoup

from . import ROOT_DIR, SESSION, ICON_DIR, CACHE_DIR
from .dither import dither

logger = getLogger(__name__)

LINKS_PAGE = ROOT_DIR / 'pages' / 'links.md'


def dl_profile_pic(channel_name: str) -> Path:
    url = f'https://www.youtube.com/@{channel_name}'
    logger.debug(f'Finding image for {channel_name}')

    response = SESSION.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    og_image = soup.find('meta', {'property': 'og:image'})
    if not og_image:
        logger.error(f'Could not find image for {channel_name}')
        return None

    image_url = og_image['content']
    image_response = SESSION.get(image_url)
    image_response.raise_for_status()

    out_file = CACHE_DIR / f'{channel_name.lower()}.jpg'
    with out_file.open('wb') as f:
        f.write(image_response.content)
        logger.info(f'Downloaded image for {channel_name} to: {out_file}')
    return out_file


def get_channel_names():
    """Given a Markdown file containing YouTube channel links, get all channel names"""
    for line in LINKS_PAGE.read_text().splitlines():
        # Look for both explicit links and yt-channel directives
        if match := re.search(r'\(https://www.youtube.com/@(.+?)\)', line):
            yield match.group(1)
        elif match := re.search(r':yt-channel:\s+(.+)\s*', line):
            yield match.group(1)


if __name__ == '__main__':
    for channel_name in get_channel_names():
        path = dl_profile_pic(channel_name)
        if path:
            dither(path, ICON_DIR, colors=32, width=128)
