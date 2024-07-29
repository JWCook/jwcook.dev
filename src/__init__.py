from datetime import timedelta
from logging import basicConfig
from os import environ
from pathlib import Path

from requests_cache import CachedSession

basicConfig(level='INFO')

ROOT_DIR = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT_DIR / 'cache'
HTML_DIR = ROOT_DIR / 'build' / 'html'
PAGES_DIR = ROOT_DIR / 'pages'
ICON_DIR = ROOT_DIR / 'assets' / 'images' / 'icons'
BASE_URL = 'https://jwcook.dev'

CACHE_DIR.mkdir(exist_ok=True, parents=True)
SESSION = CachedSession(
    CACHE_DIR / 'requests.db',
    expire_after=timedelta(days=7),
    stale_if_error=True,
)

# Should be 'local', 'dev', or 'prod'
PUBLISH_ENV = environ.get('PUBLISH_ENV', 'local')
