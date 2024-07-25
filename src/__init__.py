from os import environ
from pathlib import Path
from logging import basicConfig

basicConfig(level='INFO')

ROOT_DIR = Path(__file__).resolve().parent.parent
HTML_DIR = ROOT_DIR / 'build' / 'html'
PAGES_DIR = ROOT_DIR / 'pages'
BASE_URL = 'https://jwcook.dev'


# Should be 'local', 'dev', or 'prod'
PUBLISH_ENV = environ.get('PUBLISH_ENV', 'local')
