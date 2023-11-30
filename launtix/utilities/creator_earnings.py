#!/usr/bin/env python3

"""
This is a utility that calculates the creator earnings for a sale.
"""
def calculate(robux: int) -> int:
    # 30% of the robux is taken by Roblox.
    # We are using int instead of floor because Robux cannot be negative, and it provides faster computation.
    return int(robux * 0.7)
