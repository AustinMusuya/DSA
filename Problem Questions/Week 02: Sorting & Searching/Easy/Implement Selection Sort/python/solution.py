"""
# Selection Sort

## Problem Statement

Implement the **Selection Sort** algorithm on an array of integers `nums`.

Return the sorted array in **ascending order**.

---

## Example

**Input:**  
`nums = [29, 10, 14, 37, 13]`

**Output:**  
`[10, 13, 14, 29, 37]`

---

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

- Repeatedly select the smallest element from the unsorted portion and swap it into the correct position.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)

"""

# Sorting algorithm with fewest number of swaps. However still has a time complexity on O(n^2)
from typing import List


def selection_sort(array: List[int]) -> List[int]:
    # Edge case: Singel element or empty array
    if len(array) <= 1:
        return array

    # Nested loop mechanism updating the min value
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j  # new min element index
        # swap element with the new min
        array[i], array[min] = array[min], array[i]

    return array


print(selection_sort([29, 10, 14, 37, 13]))

print(selection_sort([2, 6, 7, 64, 654, 7, 5, 4, 9, 7,
      2, 3, 1, 6, 8, 5, 10, 11, 29, 10, 14, 37, 13]))

print(selection_sort([15]))

print(selection_sort([]))
