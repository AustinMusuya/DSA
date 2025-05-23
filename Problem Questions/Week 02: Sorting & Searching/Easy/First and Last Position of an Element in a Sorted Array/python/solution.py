"""
# First and Last Position in Sorted Array

## Problem Statement

Given a sorted array of integers `nums` and a target value `target`, return the **starting and ending position** of `target`.

If the target is not found in the array, return `[-1, -1]`.

---

## Example

**Input:**  
`nums = [5, 7, 7, 8, 8, 10], target = 8`

**Output:**  
`[3, 4]`

---

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i], target <= 10^9`
- `nums` is sorted in ascending order

---

## Approach

- Perform binary search twice:
  - Once to find the **first** occurrence
  - Once to find the **last** occurrence

---

## Desired Time & Space Complexity

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

"""

# Approach we implement the classic binary search twice for the first and the second time.

from typing import List


def first_and_second(array: List[int], target: int) -> List[int]:
    # Edge case: empty array
    if not array:
        return array
    # Implement binary search twice for the first occurence,
    # and for the second occurrence of the target value

    def find_first():
        left, right = 0, len(array) - 1
        first = -1

        while left <= right:
            mid = (left + right) // 2

            if array[mid] == target:
                first = mid
                right = mid - 1  # keep searching left
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return first

    # Second occurence
    def find_second(first_index: int):
        left, right = first_index + 1, len(array) - 1
        second = -1

        while left <= right:
            mid = (left + right) // 2
            if array[mid] == target:
                second = mid
                right = mid - 1  # look for earlier second
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return second

    first_index = find_first()
    if first_index == -1:
        return [-1, -1]

    second_index = find_second(first_index)
    return [first_index, second_index if second_index != -1 else -1]


print(first_and_second([5, 7, 7, 8, 8, 10], 8))

print(first_and_second([5, 7, 7, 8, 8, 10], 7))

print(first_and_second([5, 7, 7, 10], 8))

print(first_and_second([5, 7, 7, 8, 10], 8))
