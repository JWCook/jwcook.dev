#!/usr/bin/env python
"""Script to download favicons for links"""

import re
from logging import getLogger
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from requests import RequestException, Response

from . import ROOT_DIR, SESSION

logger = getLogger(__name__)
BLOGROLL_PAGE = ROOT_DIR / 'pages' / 'blogroll.md'
OUTPUT_DIR = ROOT_DIR / 'assets' / 'images' / 'favicons'


def download_favicon(url: str) -> Optional[Path]:
    """Download the favicon for a given URL. If it's unreachable, look for a cached version."""
    try:
        out_file = _download_favicon(url)
    except RequestException as e:
        logger.info(e)
        out_file = None

    if out_file:
        return out_file

    out_file = OUTPUT_DIR / _get_filename(url)
    if out_file.exists():
        logger.info(f'Found default favicon for {url}: {out_file}')
        return out_file
    else:
        logger.warning(f'Could not find favicon for {url}')
        return None


def _download_favicon(url: str) -> Optional[Path]:
    """Download the favicon for a given URL"""

    logger.info(f'Finding favicon for {url}')
    response = SESSION.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get favicon URL
    if (favicon := soup.find('link', rel='icon')) is None:
        favicon = soup.find('link', rel='shortcut icon')
    if not favicon:
        return None

    # Handle relative URLs
    favicon_url = favicon.get('href')
    if not favicon_url.startswith('http'):
        parsed_url = urlparse(url)
        favicon_url = f'{parsed_url.scheme}://{parsed_url.netloc}/{favicon_url.lstrip("/")}'

    # Download favicon
    response = SESSION.get(favicon_url)
    response.raise_for_status()

    out_file = OUTPUT_DIR / _get_filename(url, response)
    with out_file.open('wb') as f:
        f.write(response.content)
    logger.info(f'Favicon for {url} downloaded to {out_file}')
    return out_file


def _get_filename(parent_url: str, response: Optional[Response] = None) -> str:
    """Get base filename from original site URL, and extension from response headers"""
    base_name = urlparse(parent_url).netloc.replace('www.', '')
    if response is None:
        return f'{base_name}.png'

    if (content_disposition := response.headers.get('content-disposition')) and (
        match := re.match(r'.*filename="(.+?)".*', content_disposition)
    ):
        file_ext = match.group(1).split('.')[-1]
    else:
        file_ext = response.headers.get('content-type').split('/')[-1]
    file_ext = (
        file_ext.replace('vnd.microsoft.icon', 'ico')
        .replace('x-ico', 'ico')
        .replace('svg+xml', 'svg')
    )
    return f'{base_name}.{file_ext}'


def get_links():
    """Scrape external links from a Markdown document"""
    for line in BLOGROLL_PAGE.read_text().splitlines():
        if match := re.search(r'\[(.+?)\]\((https?://.+?)\)', line):
            parsed_url = urlparse(match.group(2))
            yield f'{parsed_url.scheme}://{parsed_url.netloc}'


if __name__ == '__main__':
    for link in set(get_links()):
        download_favicon(link)
