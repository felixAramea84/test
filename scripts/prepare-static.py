"""Copy the canonical HTML page into the Sites static directory."""
from pathlib import Path
import shutil
root = Path(__file__).resolve().parents[1]
(root / 'dist').mkdir(exist_ok=True)
shutil.copyfile(root / 'index.html', root / 'dist/index.html')
print('Prepared dist/index.html from index.html')
