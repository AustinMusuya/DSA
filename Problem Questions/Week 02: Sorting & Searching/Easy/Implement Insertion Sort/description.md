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
