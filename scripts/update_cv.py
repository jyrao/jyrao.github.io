#!/usr/bin/env python3
"""Copy the latest dated *_web.pdf in each CV language folder to stable site URLs."""
from pathlib import Path
import re
import shutil
import json

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path('/Users/jiayuanrao/StartUp/个人简历/简历终稿')

def main():
    selected = {}
    for language, folder in [('English', '英文'), ('Chinese', '中文')]:
        candidates = []
        for path in (SOURCE / folder).glob('*_web.pdf'):
            match = re.search(r'(\d{6})_web\.pdf$', path.name)
            if match:
                candidates.append((match.group(1), path))
        if not candidates:
            raise FileNotFoundError(f'No dated *_web.pdf in {SOURCE / folder}')
        date, source = max(candidates, key=lambda item: (item[0], item[1].stat().st_mtime))
        selected[language] = (date, source)
    out = ROOT / 'files/cv'
    out.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for language, (date, source) in selected.items():
        target = out / f'Jiayuan-Rao-CV-{language}_web.pdf'
        shutil.copy2(source, target)
        manifest[language] = {'date': date, 'source_filename': source.name, 'site_file': target.name}
        print(f'{language}: {source.name} -> {target.relative_to(ROOT)}')
    (out / 'versions.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')

if __name__ == '__main__':
    main()
