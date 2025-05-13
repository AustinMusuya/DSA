"""
# Check if Array is Sorted

## Problem Statement

Given an array of integers, determine if the array is sorted in **non-decreasing order**.

---

## Example

**Input:**  
`nums = [1, 2, 3, 4, 5]`  
**Output:**  
`true`

**Input:**  
`nums = [1, 3, 2, 4]`  
**Output:**  
`false`

---

## Constraints

- `1 <= nums.length <= 10^5`
"""

# An array sorted in non decreasing order would mean that nums[i] will always be smaller than nums[i+1]
# We could loop through the array and find a scenario where this isn't the case.
# If the loop is successful, then the array is sorted, if we have a mismatch, then we can return false.
from typing import List


def check_sorted(array: List[int]) -> bool:
    # edge cases: Empty or single value in array
    if (len(array) <= 1):
        return True

    # loop through the array
    size = len(array)

    for i in range(size - 1):
        if array[i] > array[i+1]:
            return False
    return True


print(check_sorted([1, 2, 3, 4, 5]))
print(check_sorted([1, 3, 2, 4]))
print(check_sorted([5]))  # in case of an array with a single element
print(check_sorted([]))  # in case of an empty array
print(check_sorted([2, 2, 2, 2]))

# Time Complexity : O(n)
# Space Complexity: O(1)
