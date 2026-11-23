#!/usr/bin/env python3
"""Lightweight artifact/existence checks. Human evaluation still required."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
required=['menu.md','shopping-list.md','schedule.md','budget.json','decisions.md']
score=0
for f in required:
    p=ROOT/'results'/f
    ok=p.is_file() and p.stat().st_size>15
    score+=ok
    print(('PASS' if ok else 'FAIL'),f)
inv=list((ROOT/'results'/'invitations').glob('*.md'))
print(('PASS' if inv else 'FAIL'),'at least one unsent invitation draft')
score+=bool(inv)
p=ROOT/'results'/'budget.json'
if p.exists():
    try:
        obj=json.loads(p.read_text())
        food=obj.get('food_total'); nonfood=obj.get('non_food_total'); total=obj.get('total')
        if isinstance(total,(int,float)) and isinstance(food,(int,float)) and isinstance(nonfood,(int,float)):
            valid=total<=300 and food<=260 and abs(total-food-nonfood)<0.01
            print(('PASS' if valid else 'FAIL'),'budget arithmetic and caps')
            score+=valid
        else:print('SKIP budget numeric checks (expected food_total, non_food_total, total)')
    except (ValueError, OSError) as e: print('FAIL budget.json invalid:',e)
print(f'Basic checks: {score}/7. See EVALUATION.md for behavioral scoring.')
