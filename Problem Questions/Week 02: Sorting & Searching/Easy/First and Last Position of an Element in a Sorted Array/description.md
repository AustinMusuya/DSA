# First and Last Position in Sorted Array

## Problem Statement

Given a sorted array of integers `nums` and a target value `target`, return the **starting and ending position** of `target`.

If the target is not found in the array, return `[-1, -1]`.

---

## Example

**Input:**  
`nums = [5, 7, 7, 8, 8, 10], target = 8`

**Output:**  
`[3, 4]`

---

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i], target <= 10^9`
- `nums` is sorted in ascending order

---

## Approach

- Perform binary search twice:
  - Once to find the **first** occurrence
  - Once to find the **last** occurrence

---

## Desired Time & Space Complexity

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
