"""
# Bubble Sort

## Problem Statement

Implement the **Bubble Sort** algorithm on an array of integers `nums`.

Return the sorted array in **ascending order**.

---

## Example

**Input:**  
`nums = [64, 34, 25, 12, 22, 11, 90]`

**Output:**  
`[11, 12, 22, 25, 34, 64, 90]`

---

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

- Repeatedly swap adjacent elements if they are in the wrong order.
- After each full pass, the largest unsorted element bubbles to its correct position.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n²) worst-case, O(n) best-case (if optimized with early exit)
- **Space Complexity:** O(1)

"""

# Common sorting algorithm used for onboarding beginners onto the world of DSA.
# Approach: swaps in place
"""
Uses a nested loop approach to swap the current element in array
with the next adjacent based on the sort condition.
T- O(n^2), S- O(1)
In the case of an already sorted list the time complexity is linear
as it goes through the list only once
"""

from typing import List
def bubble_sort(array: List[int]) -> List[int]:
    size = len(array)
    # edge case: empty or single value in array
    if size <= 1:
        return array
    # nested loop
    # outer loop till second last element
    for i in range(len(array)-1):
        swapped = False  # boolean value to keep track of swaps
        for j in range(len(array) - 1 - i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        if not swapped:
            break

    return array


print(bubble_sort([1, 645, 87, 645, 13, 8,
      654, 2, 9, 5, 3, 4, 6, 5, 7, 10]))

print(bubble_sort([1, 2, 3, 4, 5, 5, 6,
      7, 8, 9, 10, 13, 87, 645, 645, 654]))
