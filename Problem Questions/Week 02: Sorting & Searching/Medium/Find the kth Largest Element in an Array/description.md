# Kth Largest Element in an Array

## Problem Statement

Given an array of integers `nums` and an integer `k`, return the **kth largest** element in the array.

---

## Example

**Input:**  
`nums = [3, 2, 1, 5, 6, 4], k = 2`

**Output:**  
`5`

---

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## Approach

- Use a min-heap of size `k`, or use QuickSelect algorithm for better performance on average.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n) average (QuickSelect), O(n log k) with heap
- **Space Complexity:** O(1) for QuickSelect, O(k) for heap
