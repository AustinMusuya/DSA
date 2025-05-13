"""
# Remove Duplicates from Sorted Array

## Problem Statement

Given a **sorted** array of integers, remove the **duplicates in-place** such that each element appears only once and return the new length.

The relative order of the elements should be kept the same.

---

## Example

**Input:**  
`nums = [1, 1, 2, 2, 3]`

**Output:**  
`[1, 2, 3]`, new length = 3

---

## Constraints

- `1 <= nums.length <= 10^5`
- The array is sorted in non-decreasing order.

---

## Approach

- Use two pointers: `i` for the current unique element and `j` for scanning the array.
- If `nums[j] != nums[i]`, increment `i` and assign `nums[i] = nums[j]`.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

"""

# Here we use two pointer approach, where the next element is compared to the previous unique element.
# If they aren't equal, then we move an index forward from the last unique element, and change value at the current position to our new unique element.
# once the loop is done we slice out the unique part of the array
from typing import List


def remove_duplicates(array: List[int]) -> str:
    if len(array) <= 1:
        return f"{array}, new length = {len(array)}"

    j = 0  # Last unique element index

    for i in range(1, len(array)):
        if array[i] != array[j]:
            j += 1
            array[j] = array[i]

    # Slice array to unique elements only
    return f"{array[:j + 1]}, new length = {j + 1}"


print(remove_duplicates([1, 1, 2, 2, 3]))
print(remove_duplicates([1, 2, 3]))
print(remove_duplicates([1]))
print(remove_duplicates([]))
