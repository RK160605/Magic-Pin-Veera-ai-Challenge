# Vera Bot — magicpin AI Challenge
import sys
from pathlib import Path

# Ensure package directory is in sys.path
_PKG_DIR = Path(__file__).resolve().parent
if str(_PKG_DIR) not in sys.path:
    sys.path.insert(0, str(_PKG_DIR))

from .bot import app

__all__ = ["app"]
