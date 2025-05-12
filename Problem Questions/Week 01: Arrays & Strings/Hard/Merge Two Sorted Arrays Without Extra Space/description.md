# Merge Two Sorted Arrays In-Place

## Problem Statement

You are given two sorted arrays `nums1` and `nums2`. Merge them **in-place** such that after the merge, both arrays are sorted.

You **cannot use extra space** (no additional arrays).

---

## Example

**Input:**  
`nums1 = [1, 3, 5, 7]`  
`nums2 = [0, 2, 6, 8, 9]`

**Output:**  
`nums1 = [0, 1, 2, 3]`, `nums2 = [5, 6, 7, 8, 9]`

---

## Constraints

- `1 <= nums1.length, nums2.length <= 10^4`
- Both arrays are sorted in non-decreasing order.

---

## Approach

- Use the **Gap Method** (Shell Sort-like strategy):
  - Calculate an initial gap and compare elements that are `gap` apart.
  - Keep reducing the gap and repeat comparisons and swaps until gap = 0.

---

## Desired Time & Space Complexity

- **Time Complexity:** O((n + m) log(n + m))
- **Space Complexity:** O(1)
