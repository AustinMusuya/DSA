# Find Maximum and Minimum in Array

## Problem Statement

Given an array of integers, return the **maximum** and **minimum** elements in the array.

---

## Example

**Input:**  
`nums = [3, 1, 5, 9, 0, -3]`

**Output:**  
`max = 9, min = -3`

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

- Initialize two variables `min` and `max` with the first element of the array.
- Iterate through the array:
  - If the current value is less than `min`, update `min`.
  - If the current value is greater than `max`, update `max`.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n) — single pass through the array.
- **Space Complexity:** O(1) — no extra data structures required.
