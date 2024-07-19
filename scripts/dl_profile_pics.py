#!/usr/bin/env python
"""Script to download YouTube profile pics.
This allows serving smaller compressed images along with the site, to limit external requests.
"""

import re
from argparse import ArgumentParser
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


def dl_profile_pic(channel_name: str, overwrite: bool = False) -> Path:
    url = f'https://www.youtube.com/@{channel_name}'
    out_file = OUTPUT_DIR / f'{channel_name.lower()}.jpg'
    if out_file.exists() and not overwrite:
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
        # Look for both explicit links and yt-channel directives
        if match := re.search(r'\(https://www.youtube.com/@(.+?)\)', line):
            yield match.group(1)
        elif match := re.search(r':yt-channel:\s+(.+)\s*', line):
            yield match.group(1)


def main():
    parser = ArgumentParser(description='Download and process external thumbnails')
    parser.add_argument('--force', '-f', action='store_true', help='Overwrite download images')
    args = parser.parse_args()

    for channel_name in get_channel_names():
        path = dl_profile_pic(channel_name, overwrite=args.force)
        if path:
            dither(path, OUTPUT_DIR_PROCESSED, colors=32, width=128)


if __name__ == '__main__':
    main()
