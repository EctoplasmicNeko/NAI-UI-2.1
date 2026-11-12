from pathlib import Path
import json
from data.paths import SAVE_DIR
config_file_path = SAVE_DIR / "save.json"

def save_config(state):
    with config_file_path.open("w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

def load_config():
    with open(config_file_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    return config

def update_config(path: str, value):
    if config_file_path.exists():
        with config_file_path.open("r", encoding="utf-8") as f:
            config = json.load(f)
    else:
        config = {}

    keys = path.split(".")
    current = config
    for key in keys[:-1]:
        if key not in current or not isinstance(current[key], dict):
            current[key] = {}
        current = current[key]

    current[keys[-1]] = value

    with config_file_path.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)