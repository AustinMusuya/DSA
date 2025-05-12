# Longest Increasing Subsequence

## Problem Statement

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

---

## Example

**Input:** `nums = [10,9,2,5,3,7,101,18]`  
**Output:** `4`  
**Explanation:** The LIS is `[2,3,7,101]`.

---

## Constraints

- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4

---

## Approach

- Use dynamic programming with binary search or a bottom-up DP array.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n log n) (with binary search), O(n^2) (pure DP)
- **Space Complexity:** O(n)
