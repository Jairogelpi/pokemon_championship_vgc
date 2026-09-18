#!/usr/bin/env python3
"""Validate documentation integrity; this does not validate the product."""
from pathlib import Path
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
def require(condition, message):
    if not condition:
        errors.append(message)

def read(path):
    return (ROOT / path).read_text(encoding='utf-8')

original = ROOT / 'docs/source/V1_SPEC_ORIGINAL.md'
provenance = read('docs/source/PROVENANCE.md')
expected_hash = re.search(r'SHA-256: `([a-f0-9]{64})`', provenance)
require(expected_hash is not None, 'Missing source SHA-256')
if expected_hash:
    require(hashlib.sha256(original.read_bytes()).hexdigest() == expected_hash[1], 'Original source bytes changed')
source = original.read_text(encoding='utf-8')
sections = re.findall(r'^## (\d+)\. ', source, re.M)
require(sections == [str(n) for n in range(62)], 'Expected original sections 0..61')
requirements = read('docs/product/REQUIREMENTS.md')
trace = read('docs/quality/TRACEABILITY.md')
for n in range(62):
    rid = f'REQ-S{n:02}'
    require(len(re.findall(r'^## '+rid+r'\b', requirements, re.M)) == 1, f'{rid}: missing/duplicate requirement')
    require(len(re.findall(r'^\| '+rid+r' \|', trace, re.M)) == 1, f'{rid}: missing/duplicate trace row')
    rows = re.findall(r'^\| '+rid+r' \|.*$', trace, re.M)
    if rows:
        spec = re.search(r'\]\(\.\./\.\./(specs/[^)]+)\)', rows[0])
        require(spec is not None, f'{rid}: no spec mapping')
        if spec and (ROOT/spec[1]).exists():
            require(rid in read(spec[1]), f'{rid}: absent from assigned spec')
dod_source = source.split('## 59. V1 Definition of Done')[1].split('## 60.')[0]
dod = re.findall(r'^\d+\.\s+(.+)$', dod_source, re.M)
acceptance = read('docs/quality/V1_ACCEPTANCE.md')
require(len(dod) == 34, 'Expected 34 original acceptance criteria')
for i, wording in enumerate(dod, 1):
    prefix = f'| AC-V1-{i:02} | {wording} |'
    require(acceptance.count(prefix) == 1, f'AC-V1-{i:02}: criterion missing or changed')

detailed = read('docs/quality/DETAILED_COVERAGE.md')
subreqs = re.findall(r'^- \[[ xX]\] (REQ-S\d{2}-\d{2}): (.+)$', detailed, re.M)
require(len(subreqs) == len(set(rid for rid, _ in subreqs)), 'Duplicate detailed requirement IDs')
for n in range(62):
    rid = f'REQ-S{n:02}'
    require(len(re.findall(r'^## '+rid+r'\b', detailed, re.M)) == 1, f'{rid}: missing detailed coverage section')
    require(any(sub.startswith(rid+'-') for sub, _ in subreqs), f'{rid}: missing detailed checks')
for spec_file in (ROOT/'specs').glob('*/spec.md'):
    require('DETAILED_COVERAGE.md' in spec_file.read_text(encoding='utf-8'), f'{spec_file.parent.name}: missing detailed gate')

files = list(ROOT.rglob('*.md'))
seen = {}
for path in files:
    relative = path.relative_to(ROOT).as_posix()
    require(relative.casefold() not in seen, f'Case-insensitive filename collision: {relative}')
    seen[relative.casefold()] = relative
    # Ignore fenced examples; validate file links, not anchors or remote resources.
    content = re.sub(r'```.*?```', '', path.read_text(encoding='utf-8'), flags=re.S)
    for target in re.findall(r'\]\(([^)]+)\)', content):
        target = target.split('#')[0]
        if not target or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target):
            continue
        require((path.parent / target).exists(), f'Broken local link in {relative}: {target}')

skills = list((ROOT / '.agents/skills').glob('*/SKILL.md'))
require(len(skills) == 8, 'Expected 8 project skills')
for path in skills:
    text = path.read_text(encoding='utf-8')
    front = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    require(front is not None, f'{path.parent.name}: missing skill frontmatter')
    if front:
        require(f'name: {path.parent.name}\n' in front[1]+'\n', f'{path.parent.name}: skill name mismatch')
        require(bool(re.search(r'^description: .+', front[1], re.M)), f'{path.parent.name}: missing description')
        require(bool(re.fullmatch(r'[a-z0-9-]{1,64}',path.parent.name)), f'{path.parent.name}: invalid name')
require(len(list((ROOT / 'specs').glob('*/spec.md'))) == 16, 'Expected 16 implementation specs')
if errors:
    print('\n'.join('FAIL: '+e for e in errors))
    sys.exit(1)
print(f'PASS: source SHA-256; 62 requirements and trace mappings; 34 original acceptance criteria; {len(subreqs)} detailed checks; {len(files)} Markdown files; local links; 8 skills; 16 specs.')
print('Product implementation, mechanics, Vitest and performance: NOT VERIFIED by this command.')
