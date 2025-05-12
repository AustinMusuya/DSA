# Maximum Subarray (Kadane's Algorithm)

## Problem Statement

Given an integer array `nums`, find the contiguous subarray with the largest sum and return its sum.

---

## Example

**Input:** `nums = [-2,1,-3,4,-1,2,1,-5,4]`  
**Output:** `6`  
**Explanation:** The subarray `[4,-1,2,1]` has the largest sum.

---

## Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

---

## Approach

- Use Kadane’s Algorithm to track the current and global maximum as you iterate.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
