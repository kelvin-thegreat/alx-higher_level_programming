#!/usr/bin/python3
import sys

args = sys.argv[1:]
num_args = len(args)

print(f"{num_args} argument{'s' if num_args != 1 else ''}: ", end="")
if num_args == 0:
    print(".")
elif num_args == 0:
    print(":")
else:
    print("")
    for i, arg in enumerate(args):
        print(f"{i+1} {arg}")
