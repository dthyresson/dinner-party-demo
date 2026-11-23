#!/usr/bin/env python3
"""Inject an immutable fictional event into local inbox."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
EVENTS = {'late_guest': 'late_guest.md', 'stock_change': 'second_disruption.md'}
if len(sys.argv)!=2 or sys.argv[1] not in EVENTS:
    print('Usage: python3 scripts/inject.py late_guest|stock_change')
    sys.exit(2)
event=sys.argv[1]
out=ROOT/'messages'/'inbox'/f'{event}.md'
if out.exists():
    print('Already injected:',out.relative_to(ROOT))
    sys.exit(1)
out.write_text((ROOT/'fixtures'/EVENTS[event]).read_text())
print('Injected',out.relative_to(ROOT))
print('Notify Chief of Staff / Guest Manager' if event=='late_guest' else 'Notify Chief of Staff / Procurement')
