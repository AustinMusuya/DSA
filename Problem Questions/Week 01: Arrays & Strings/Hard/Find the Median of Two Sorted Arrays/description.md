# Median of Two Sorted Arrays

## Problem Statement

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the **median** of the two sorted arrays.

The overall run time complexity should be **O(log (m+n))**.

---

## Example

**Input:**  
`nums1 = [1, 3]`  
`nums2 = [2]`

**Output:**  
`2.0`

---

## Constraints

- `0 <= nums1.length, nums2.length <= 1000`
- `1 <= nums1.length + nums2.length <= 2000`
- Arrays are sorted in non-decreasing order.

---

## Approach

- Use **binary search on the smaller array** to partition both arrays.
- Ensure elements on the left are <= elements on the right.
- Handle both even and odd total lengths properly.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(log(min(m, n))) — binary search on the shorter array
- **Space Complexity:** O(1)
