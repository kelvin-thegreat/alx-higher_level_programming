#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)  # make sure tuple_a has at least 2 integers
    b = tuple_b + (0, 0)  # make sure tuple_b has at least 2 integers
    return (a[0] + b[0], a[1] + b[1])
