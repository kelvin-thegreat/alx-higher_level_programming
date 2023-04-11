#!/usr/bin/python3
"""
    checks if object is an instance of a class that
    inherited from the specified class or not
"""

def inherits_from(obj, a_class):

    """
    Check if an object is an instance of a
    class that inherited (directly or indirectly)
    from a specified class.

    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
