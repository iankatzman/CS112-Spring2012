#!/usr/bin/env python
"""
Selection sort

This is my selection sort, it's not working right!!!
I used this:
    http://en.wikipedia.org/wiki/Selection_sort
"""
from hwtools import input_nums

while True:
    try:
        nums = input_nums() # Number input.
        break

    # Error message.
    except ValueError:
        print "Please enter numbers."

# Number list.
print "Before sort:"
print nums

max_position = len(nums) # The max position of the number of elements in the list.

for current_position in range(max_position):

    current_min = current_position # The minimum number starts out as the current position.

    # Tests the position to the right of the last current position within the range of the max position.
    for test_position in range(current_position + 1 , max_position):

        # If the number in the test position is less than that of the current minimum then the current minimum becomes the testing position.
        if nums[test_position] < nums[current_min]:
            current_min = test_position

    # This swaps the current minimum for the current position after each test of each new position in the list.
    nums[current_position] , nums[current_min] = nums[current_min] , nums[current_position]

# Prints the number list after it is sorted.
print "After sort:"
print nums
