#!/usr/bin/env python
"""Script to download YouTube profile pics"""

import re
from logging import getLogger
from pathlib import Path

import requests
from bs4 import BeautifulSoup

from . import ROOT_DIR
from .dither import dither

logger = getLogger(__name__)

LINKS_PAGE = ROOT_DIR / 'pages' / 'links.md'
OUTPUT_DIR = ROOT_DIR / 'assets' / 'images' / 'cache'
OUTPUT_DIR_PROCESSED = ROOT_DIR / 'assets' / 'images' / 'profile_pics'
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)


def dl_profile_pic(channel_name: str) -> Path:
    url = f'https://www.youtube.com/@{channel_name}'
    out_file = OUTPUT_DIR / f'{channel_name.lower()}.jpg'
    if out_file.exists():
        logger.info(f'Image for {channel_name} already exists')
        return out_file

    logger.debug(f'Finding image for {channel_name}')
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    og_image = soup.find('meta', {'property': 'og:image'})
    if not og_image:
        logger.error(f'Could not find image for {channel_name}')
        return None

    image_url = og_image['content']
    image_response = requests.get(image_url)
    image_response.raise_for_status()
    with out_file.open('wb') as f:
        f.write(image_response.content)
        logger.info(f'Downloaded image for {channel_name} to: {out_file}')
    return out_file


def get_channel_names():
    """Given a Markdown file containing YouTube channel links, get all channel names"""
    for line in LINKS_PAGE.read_text().splitlines():
        if match := re.search(r'\(https://www.youtube.com/@(.+?)\)', line):
            yield match.group(1)


if __name__ == '__main__':
    for channel_name in get_channel_names():
        path = dl_profile_pic(channel_name)
        if path:
            dither(path, OUTPUT_DIR_PROCESSED, colors=32, width=128)
