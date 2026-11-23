"""Copy this edition's image into the configured output directory."""

import os
import shutil
from pathlib import Path


def main():
    """Copy entry.png from this program's directory to the output folder."""
    folder = Path(__file__).resolve().parent
    output = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output.mkdir(parents=True, exist_ok=True)
    shutil.copy2(folder / "entry.png", output / "entry.png")


if __name__ == "__main__":
    main()
