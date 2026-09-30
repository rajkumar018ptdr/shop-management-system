import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

def load_json(filename, default):
    path = DATA_DIR / filename
    if not path.exists():
        save_json(filename, default)
        return default
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return default

def save_json(filename, data):
    with (DATA_DIR / filename).open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def next_id(records, prefix):
    nums=[]
    for key in records:
        if key.startswith(prefix):
            try: nums.append(int(key[len(prefix):]))
            except ValueError: pass
    return f"{prefix}{max(nums, default=0)+1:04d}"
