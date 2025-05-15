"""
# Linear Search for Target

## Problem Statement

Given an array of integers and a target value, return the **index** of the target if it exists, or `-1` if it doesn't.

---

## Example

**Input:**  
`nums = [4, 2, 9, 7, 5]`, `target = 9`  
**Output:**  
`2`

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= target <= 10^9`

---

## Approach

- Iterate through the array.
- If `nums[i] == target`, return `i`.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

"""

from typing import List

target = 9


# A simple loop will do, comparing each element to the target value and giving its index
# In the event where the target i not found, -1 will be returned
def linear_search(array: List[int], target: int) -> int:
    # edge cases:
    # 1. incase of empty list
    if not array:
        return -1
    # loop through elements in list and compare with target value
    for i in range(len(array)):
        if array[i] == target:
            return i

    return -1


print(linear_search([4, 2, 9, 7, 5], 9))
print(linear_search([4, 2, 8, 7, 5], 9))
print(linear_search([], 9))  # empty array
print(linear_search([4], 9))
print(linear_search([9], 9))
