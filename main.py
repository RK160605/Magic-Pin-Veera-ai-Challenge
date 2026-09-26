import os
import sys
from pathlib import Path

# Add bot directory to sys.path so internal imports resolve cleanly
BASE_DIR = Path(__file__).resolve().parent
BOT_DIR = BASE_DIR / "bot"
if str(BOT_DIR) not in sys.path:
    sys.path.insert(0, str(BOT_DIR))

from bot import app

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
