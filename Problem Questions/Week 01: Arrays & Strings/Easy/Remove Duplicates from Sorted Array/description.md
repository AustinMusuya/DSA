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
