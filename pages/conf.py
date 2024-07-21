# Sphinx config stub file; actual config is in src.conf
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR))
from src.conf import *  # noqa: E402, F403, F401
