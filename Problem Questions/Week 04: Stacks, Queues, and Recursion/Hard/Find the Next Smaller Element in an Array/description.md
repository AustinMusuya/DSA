# Next Smaller Element

## Problem Statement

Given an array `nums`, for each element, find the next smaller element to its right. If no such element exists, return `-1` for that position.

---

## Example

**Input:**  
`nums = [4, 8, 5, 2, 25]`  
**Output:**  
`[2, 5, 2, -1, -1]`

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

- Use a monotonic stack (decreasing) while iterating from right to left.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
