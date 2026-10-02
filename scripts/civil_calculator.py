#!/usr/bin/env python3
"""Arithmetic helpers for CivilCode AI.

This script does NOT decide legal entitlement or the legally applicable rate.
Use only after the governing rule and inputs have been independently verified.
"""
from decimal import Decimal, ROUND_HALF_UP

D = Decimal

def money(x):
    return D(str(x)).quantize(D("0.01"), rounding=ROUND_HALF_UP)

def simple_interest(principal, annual_rate, days, year_days=365):
    """Simple interest. annual_rate is decimal, e.g. 0.0365 for 3.65%."""
    return money(D(str(principal)) * D(str(annual_rate)) * D(str(days)) / D(str(year_days)))

def proportional_loss(base_amount, proportion):
    """Arithmetic allocation only; proportion is decimal from 0 to 1."""
    return money(D(str(base_amount)) * D(str(proportion)))

def split_amount(total, shares):
    """Split total by numeric relative shares. Rounding residual goes to last item."""
    total = money(total)
    weights = [D(str(x)) for x in shares]
    if not weights or any(x < 0 for x in weights) or sum(weights) == 0:
        raise ValueError("shares must contain non-negative values with positive total")
    out=[]
    used=D("0.00")
    s=sum(weights)
    for i,w in enumerate(weights):
        if i == len(weights)-1:
            part=total-used
        else:
            part=money(total*w/s); used += part
        out.append(part)
    return out

if __name__ == "__main__":
    print("CivilCode AI arithmetic helper. Import functions after legal inputs are verified.")
