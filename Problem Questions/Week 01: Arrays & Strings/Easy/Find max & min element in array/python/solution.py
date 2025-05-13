''' 
# Find Maximum and Minimum in Array

# Problem Statement

# Given an array of integers, return the **maximum** and **minimum** elements in the array.

# Example


**Input:**  
`nums = [3, 1, 5, 9, 0, -3]`

**Output:**  
`max = 9, min = -3`
'''

from typing import List


def max_and_min(array: List[int]) -> str:
    # set the index of the first value of the array (0) to both the max and the min.
    # loop through the array once updating values of max and min
    # when a smaller or larger value is found

    if not array:  # edge case (empty array)
        return "Array is empty."

    max = 0
    min = 0
    size = len(array)

    for i in range(1, size):
        if array[i] < array[min]:
            min = i
        if array[i] > array[max]:
            max = i

    return f"max = {array[max]}, min = {array[min]}"


# Example Test Cases

nums = [3, 1, 5, 9, 0, -3]

nums2 = [3, 1, 5, 9, 0, -3, 6, 12, 4, 687, 654, 312, -4, -15, -213]

nums3 = [5]  # in the case of a single element in the array

nums4 = []  # in the case of an empty array

print(max_and_min(nums))
print(max_and_min(nums2))
print(max_and_min(nums3))
print(max_and_min(nums4))


# Time Complexity : O(n)
# Space Complexity: O(1)
