# Peak Element

## Problem Statement

A **peak element** is an element that is strictly greater than its neighbors.

Given an array `nums`, find a peak element and return its index.

You may assume that `nums[-1] = nums[n] = -∞` (virtual boundaries).

---

## Example

**Input:**  
`nums = [1, 2, 3, 1]`

**Output:**  
`2`  
**Explanation:** `nums[2] = 3` is a peak

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

- Use binary search by comparing mid element with its neighbors.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
