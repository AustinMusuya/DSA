"""
# Insertion Sort

## Problem Statement

Implement the **Insertion Sort** algorithm on an array of integers `nums`.

Return the sorted array in **ascending order**.

---

## Example

**Input:**  
`nums = [5, 2, 9, 1, 5, 6]`

**Output:**  
`[1, 2, 5, 5, 6, 9]`

---

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

- Start from index 1 and insert each element into its correct position in the sorted left subarray.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n²) worst-case, O(n) best-case (nearly sorted)
- **Space Complexity:** O(1)

"""

"""
The approach here is similar to how you sort cards in your hand: you pick the next card (element),
compare it with the ones already sorted (to its left), and insert it in the correct position
by shifting larger elements to the right.

We move through the array from left to right, assuming that the portion on the left is already sorted.
At each step, we take the "key" (the current value), and compare it with elements to its left.
As long as those elements are larger than the key, we shift them one position to the right.
Once we find the correct spot, we insert the key.

This method avoids repeated swapping and is more efficient than a purely swap-based version.
"""


from typing import List
def insertion_sort(array: List[int]) -> List[int]:
    # Edge case: Empty or single value in array
    if len(array) <= 1:
        return array

    # Nested loop approach O(n^2) Time Complexity
    for i in range(1, len(array)):
        key = array[i]

        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]  # shift value if condition is true
            j -= 1
        array[j+1] = key

    return array


print(insertion_sort([5, 2, 9, 1, 5, 6]))
print(insertion_sort([]))
print(insertion_sort([5, 2, 9, 1, 5, 6, 0, 0, 0]))
print(insertion_sort([5]))
