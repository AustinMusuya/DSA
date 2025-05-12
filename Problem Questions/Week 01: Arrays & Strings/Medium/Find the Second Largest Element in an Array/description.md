# Second Largest Element in Array

## Problem Statement

Given an array of integers, find the **second largest distinct element** in the array.

If no such element exists, return an appropriate sentinel value (e.g., `-1` or `null`).

---

## Example

**Input:**  
`nums = [12, 35, 1, 10, 34, 1]`

**Output:**  
`34`

---

## Constraints

- `2 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

- Initialize `max` and `secondMax`.
- Iterate through the array, updating both as needed, while skipping duplicates.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
