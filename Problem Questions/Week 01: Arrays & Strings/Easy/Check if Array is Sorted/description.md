# Check if Array is Sorted

## Problem Statement

Given an array of integers, determine if the array is sorted in **non-decreasing order**.

---

## Example

**Input:**  
`nums = [1, 2, 3, 4, 5]`  
**Output:**  
`true`

**Input:**  
`nums = [1, 3, 2, 4]`  
**Output:**  
`false`

---

## Constraints

- `1 <= nums.length <= 10^5`

---

## Approach

- Loop through the array:
  - If at any index `i`, `nums[i] > nums[i+1]`, return `false`.
- If the loop completes, the array is sorted.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
