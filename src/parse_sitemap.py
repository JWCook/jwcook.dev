from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree

from . import PAGES_DIR

BUILD_DIR = Path(__file__).parent.parent / 'build' / 'html'
OUTPUT_FILE = PAGES_DIR / 'sitemap2.md'


def parse_urls() -> list[str]:
    """Parse an XML sitemap and return a list of URLs"""
    sitemap_xml = (BUILD_DIR / 'sitemap.xml').read_text()
    root = ElementTree.fromstring(sitemap_xml)
    urls = root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
    return [url.text for url in urls]


def build_sitemap():
    urls = parse_urls()
    paths = [urlparse(url).path.replace('.html', '') for url in urls]
    # Build a list of markdown links
    with OUTPUT_FILE.open('w') as f:
        f.write('# {fas}`sitemap` Sitemap\n')
        for path in sorted(paths):
            f.write(f'- [{path}]({path})\n')


if __name__ == '__main__':
    build_sitemap()
