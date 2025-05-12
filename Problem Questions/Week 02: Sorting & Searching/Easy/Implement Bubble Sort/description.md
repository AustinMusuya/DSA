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
