#!/usr/bin/env python3
import os
import re
from pathlib import Path

ROOT = Path('.').resolve()
pattern = re.compile(r"\(<([^>]+)>\)")

missing = []

for md in ROOT.rglob('*.md'):
    try:
        text = md.read_text(encoding='utf-8')
    except Exception:
        continue
    for m in pattern.finditer(text):
        target = m.group(1)
        # ignore URLs
        if target.startswith('http://') or target.startswith('https://'):
            continue
        # If target is absolute (starts with /), consider from repo root
        if target.startswith('/'):
            candidate = (ROOT / target.lstrip('/')).resolve()
        else:
            candidate = (md.parent / target).resolve()
        if not candidate.exists():
            missing.append((str(md.relative_to(ROOT)), target, str(candidate)))

if not missing:
    print('No missing link targets found.')
else:
    print('Missing link targets:')
    for md, targ, cand in missing:
        print(f'- In {md}: target "{targ}" -> resolved path: {cand} (MISSING)')
    print('\nTotal missing:', len(missing))
