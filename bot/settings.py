from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE = {
    'NAME': BASE_DIR / 'db.sqlite3'
}
