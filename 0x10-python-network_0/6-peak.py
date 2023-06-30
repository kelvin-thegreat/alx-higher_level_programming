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

    # Call the recursive function to find the peak within the entire list
    return find_peak_recursive(list_of_integers, 0, size - 1)


def find_peak_recursive(list_of_integers, start, end):
    """
    Recursively finds a peak within a specific range of the list.

    Args:
        list_of_integers (list): List of integers to search for a peak.
        start (int): The starting index of the range.
        end (int): The ending index of the range.

    Returns:
        int: The peak element within the specified range.
    """
    if start == end:
        # Base case: When the range contains only one element, return that element as the peak
        return list_of_integers[start]

    mid = (start + end) // 2

    if list_of_integers[mid] < list_of_integers[mid + 1]:
        # If the middle element is smaller than the next element,
        # the peak must exist in the subarray to the right
        return find_peak_recursive(list_of_integers, mid + 1, end)
    else:
        # If the middle element is greater than or equal to the next element,
        # the peak must exist in the subarray to the left
        return find_peak_recursive(list_of_integers, start, mid)

