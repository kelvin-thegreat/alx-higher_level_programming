#!/usr/bin/python3
"""

Module composed by a function that prints 2 new lines after ".?:" characters

"""


def text_indentation(text):

    """ Function that prints 2 new lines after ".?:" characters

    Args:
        text: input string

    Returns:
        No return

    Raises:
        TypeError: If text is not a string


    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in [".", "?", ":"]:
        text = text.replace(char, char + "\n\n")

    """Remove any leading/trailing whitespace"""
    text = text.strip()

    """Print the resulting text"""
    print(text)

