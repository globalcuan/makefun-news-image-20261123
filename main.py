import os
import shutil
from pathlib import Path

source = Path(__file__).with_name('entry.png')
out = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
os.makedirs(out, exist_ok=True)
shutil.copyfile(source, Path(out) / 'entry.png')
