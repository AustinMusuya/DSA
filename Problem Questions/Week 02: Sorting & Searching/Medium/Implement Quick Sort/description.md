# Quick Sort

## Problem Statement

Implement the **Quick Sort** algorithm to sort an array `nums` in ascending order.

Return the sorted array.

---

## Example

**Input:**  
`nums = [10, 7, 8, 9, 1, 5]`

**Output:**  
`[1, 5, 7, 8, 9, 10]`

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

- Choose a pivot.
- Partition the array such that elements less than pivot go left, greater go right.
- Recursively sort left and right halves.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n log n) average, O(n²) worst-case
- **Space Complexity:** O(log n) due to recursion stack
