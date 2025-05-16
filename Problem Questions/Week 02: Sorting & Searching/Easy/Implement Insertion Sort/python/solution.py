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

# Approach: Mechanism for this is shifting the elements in a nested loop whilst comparing with the key.
# Set a key as the first element and loop through the array comparing with the other values.
# In the event a value is greater than the key, shift the value to the right and insert the key
# at the appropriate position. Solution does in place sorting (O(1) Space Complexity)
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
