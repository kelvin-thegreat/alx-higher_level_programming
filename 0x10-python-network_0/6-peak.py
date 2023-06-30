#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using the divide and conquer strategy.

    Args:
        list_of_integers (list): List of integers to find the peak of.

    Returns:
        int or None: The peak element of the list, or None if the list is empty.
    """
    size = len(list_of_integers)

    if size == 0:
        return None
    return find_peak_recursive(list_of_integers, 0, size - 1)


def find_peak_recursive(list_of_integers, start, end):
    """
    Recursively finds a peak within a specific range

    """
    if start == end:
        return list_of_integers[start]

    mid = (start + end) // 2

    if list_of_integers[mid] < list_of_integers[mid + 1]:
                
        return find_peak_recursive(list_of_integers, mid + 1, end)
    else:

        return find_peak_recursive(list_of_integers, start, mid)

