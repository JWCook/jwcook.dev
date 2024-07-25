from datetime import timedelta
from logging import basicConfig
from os import environ
from pathlib import Path

from requests_cache import CachedSession

basicConfig(level='INFO')

ROOT_DIR = Path(__file__).resolve().parent.parent
HTML_DIR = ROOT_DIR / 'build' / 'html'
PAGES_DIR = ROOT_DIR / 'pages'
BASE_URL = 'https://jwcook.dev'

SESSION = CachedSession(ROOT_DIR / 'requests.db', expire_after=timedelta(days=7))

# Should be 'local', 'dev', or 'prod'
PUBLISH_ENV = environ.get('PUBLISH_ENV', 'local')
