#!/usr/bin/python3
def magic_calculation(a, b):
    """Match bytecode provided"""
    from magic_calculation_102 import add, sub

    if a < b:
        return sum([add(a, b) for _ in range(2)]) + add(4, 5)
    else:
        return (sub(a, b))

