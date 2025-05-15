"""
# Second Largest Element in Array

## Problem Statement

Given an array of integers, find the **second largest distinct element** in the array.

If no such element exists, return an appropriate sentinel value (e.g., `-1` or `null`).

---

## Example

**Input:**  
`nums = [12, 35, 1, 10, 34, 1]`

**Output:**  
`34`

---

## Constraints

- `2 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

- Initialize `max` and `secondMax`.
- Iterate through the array, updating both as needed, while skipping duplicates.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

"""
# We will initialize max number and the second max number.
# We iterate throught the list updating these values if any number is larger than the two maintaing
# the description of max and second max
from typing import List


def second_largest(array: List[int]) -> int:
    # edge cases: Empty list or single value in list
    if len(array) < 2:
        return -1

    first_max = 0

    for i in range(1, len(array)):
        if array[i] > array[first_max]:
            first_max = i  # find the max value in array

    # find the second_max value in array
    second_max = None
    for i in array:
        if i != array[first_max]:
            if second_max is None or i > second_max:
                second_max = i

    return second_max if second_max is not None else -1


print(second_largest([12, 35, 1, 10, 34, 1]))
print(second_largest([]))
print(second_largest([12, 35]))
print(second_largest([12]))
print(second_largest([3, 3, 3]))

# Time complexity is actually O(n+n) which translates to O(n)
# Space compmlexity remains constant
