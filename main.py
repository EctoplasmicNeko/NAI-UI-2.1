from ui.ui_main import run_app
from data import datahub
from data.paths import (
    PORTRAITS_DIR,
    OUTPUT_DIR,
    CHARACTERS_DIR,
    REFERENCE_DIR,
    ENCODES_DIR,
    VIBES_DIR
)
def ensure_dirs() -> None:
    PORTRAITS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    CHARACTERS_DIR.mkdir(parents=True, exist_ok=True)
    REFERENCE_DIR.mkdir(parents=True, exist_ok=True)
    ENCODES_DIR.mkdir(parents=True, exist_ok=True)
    VIBES_DIR.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    ensure_dirs()
    datahub.load_all()
    datahub.load_characters()
    run_app()
