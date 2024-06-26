#!/usr/bin/python3
# function that finds a peak in a list of unsorted integers.
# algorithm must have the lowest complex


def find_peak(list_of_integers):
    """ function that finds a peak in a list of unsorted integers"""

    mid = int((len(list_of_integers) / 2))
    if list_of_integers is None:
        return none
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
