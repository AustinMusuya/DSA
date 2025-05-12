# Binary Search

## Problem Statement

Given a **sorted array** of integers `nums` and an integer `target`, return the **index** of `target` if it exists, or `-1` if it does not.

---

## Example

**Input:**  
`nums = [-1, 0, 3, 5, 9, 12], target = 9`

**Output:**  
`4`

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i], target <= 10^9`
- `nums` is sorted in ascending order

---

## Approach

- Use the standard binary search pattern with two pointers: `low` and `high`.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
