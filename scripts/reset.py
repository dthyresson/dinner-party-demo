#!/usr/bin/env python3
"""Clear simulated runtime artifacts without touching seed data or role instructions."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
for d in [ROOT/'messages'/'inbox', ROOT/'messages'/'outbox', ROOT/'results'/'invitations'] + list(ROOT.glob('*/workspace')):
    for f in d.glob('*'):
        if f.is_file() and f.name!='.gitkeep':f.unlink()
for f in (ROOT/'results').iterdir():
    if f.is_file() and f.name != 'README.md':f.unlink()
(ROOT/'chief-of-staff'/'workspace'/'plan.md').write_text('# Planning workspace\n\nNo plan yet.\n')
(ROOT/'chief-of-staff'/'workspace'/'decisions.md').write_text('# Decision log\n\nNo decisions yet.\n')
print('Demo reset. Role data and fixtures preserved.')
