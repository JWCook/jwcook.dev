#!/usr/bin/env python
"""Script to download favicons for links"""
import re
from logging import getLogger
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from requests import Response

from . import ROOT_DIR

logger = getLogger(__name__)
BLOGROLL_PAGE = ROOT_DIR / 'pages' / 'blogroll.md'
OUTPUT_DIR = ROOT_DIR / 'assets' / 'images' / 'favicons'


def download_favicon(url: str):
    """Download the favicon for a given URL"""

    logger.debug(f'Finding favicon for {url}')
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get favicon URL
    if (favicon := soup.find('link', rel='icon')) is None:
        favicon = soup.find('link', rel='shortcut icon')
    if not favicon:
        logger.warning(f'Could not find favicon for {url}')
        return

    # Handle relative URLs
    favicon_url = favicon.get('href')
    if not favicon_url.startswith('http'):
        parsed_url = urlparse(url)
        favicon_url = f'{parsed_url.scheme}://{parsed_url.netloc}/{favicon_url.lstrip("/")}'

    # Download favicon
    response = requests.get(favicon_url)
    response.raise_for_status()

    out_file = OUTPUT_DIR / _get_filename(response, url)
    with out_file.open('wb') as f:
        f.write(response.content)
    logger.info(f'Favicon for {url} downloaded to {out_file}')


def _get_filename(response: Response, parent_url:str) -> str:
    """Get base filename from original site URL, and extension from response headers """
    base_name = urlparse(parent_url).netloc.replace('www.', '')
    if (
        (content_disposition := response.headers.get('content-disposition')) and
        (match := re.match(r'.*filename="(.+?)".*', content_disposition))
    ):
        file_ext = match.group(1).split('.')[-1]
    else:
        file_ext = response.headers.get('content-type').split('/')[-1]
    file_ext = file_ext.replace('vnd.microsoft.icon', 'ico')
    file_ext = file_ext.replace('x-ico', 'ico')
    return f'{base_name}.{file_ext}'


def get_links():
    """Scrape external links from a Markdown document"""
    for line in BLOGROLL_PAGE.read_text().splitlines():
        if match := re.search(r'\[(.+?)\]\((https?://.+?)\)', line):
            parsed_url = urlparse(match.group(2))
            yield f'{parsed_url.scheme}://{parsed_url.netloc}'

def main():
    for link in set(get_links()):
        download_favicon(link)

if __name__ == '__main__':
    main()