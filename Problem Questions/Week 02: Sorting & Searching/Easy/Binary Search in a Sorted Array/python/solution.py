"""
# Binary Search

## Problem Statement

Given a **sorted array** of integers `nums` and an integer `target`, return the **index** of `target` if it exists, or `-1` if it does not.

---

## Example

**Input:**  
`nums = [-1, 0, 3, 5, 9, 12], target = 9`

**Output:**  
`4`

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i], target <= 10^9`
- `nums` is sorted in ascending order

---

## Approach

- Use the standard binary search pattern with two pointers: `low` and `high`.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
"""

# To implement Binary search we consider that the value at the middle index of the array
# could be equal to our target value, less than or greater than.
# If it is equal then we return the index, if less, we discard the left half of the array
# and reassign the value of our middle index to the mid part of the right subarray.
# We do the inverse of this when it is greater.
from typing import List


def binary_search(array: List[int], target: int) -> int:

    # Edge case: if the input array is empty, there's nothing to search
    if not array:
        return -1

    # Set initial search boundaries to the full array range
    left, right = 0, len(array) - 1

    # Continue searching while there is a valid range to search
    while left <= right:
        # Compute the middle index (integer division avoids float)
        mid = (left + right) // 2

        # Compare middle element with the target
        if array[mid] == target:
            return mid  # Found the target, return its index
        elif array[mid] < target:
            # Target is in the right half → discard the left half
            left = mid + 1
        else:
            # Target is in the left half → discard the right half
            right = mid - 1

    # Target not found
    return -1


print(binary_search([-1, 0, 3, 5, 9, 12], 9))
print(binary_search([], 9))
print(binary_search([-1, 0, 3, 5, 11, 12], 9))
print(binary_search([9], 9))
