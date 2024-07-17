#!/usr/bin/env python
"""Script to download YouTube profile pics"""
import re
from logging import basicConfig, getLogger
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ROOT_DIR = Path(__file__).resolve().parent.parent
LINKS_PAGE = ROOT_DIR / 'pages' / 'links.md'
OUTPUT_DIR = ROOT_DIR / 'assets' / 'images' / 'cache'
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
logger = getLogger(__name__)
basicConfig(level='INFO')


def dl_profile_pic(channel_name:str):
    url = f"https://www.youtube.com/@{channel_name}"
    out_file = OUTPUT_DIR / f"{channel_name}.jpg"
    if out_file.exists():
        logger.info(f"Image for {channel_name} already exists")
        return

    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    og_image = soup.find("meta", {"property": "og:image"})
    if not og_image:
        logger.error(f"Could not find image for {channel_name}")
        return

    image_url = og_image["content"]
    image_response = requests.get(image_url)
    image_response.raise_for_status()
    with out_file.open("wb") as f:
        f.write(image_response.content)
        logger.info(f"Downloaded image for {channel_name}")


def get_channel_names():
    """Given a Markdown file containing YouTube channel links, get all channel names"""
    for line in LINKS_PAGE.read_text().splitlines():
        if match := re.search(r"\(https://www.youtube.com/@(.+?)\)", line):
            yield match.group(1)



if __name__ == '__main__':
    for channel_name in get_channel_names():
        dl_profile_pic(channel_name)