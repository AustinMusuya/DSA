# Linear Search for Target

## Problem Statement

Given an array of integers and a target value, return the **index** of the target if it exists, or `-1` if it doesn't.

---

## Example

**Input:**  
`nums = [4, 2, 9, 7, 5]`, `target = 9`  
**Output:**  
`2`

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= target <= 10^9`

---

## Approach

- Iterate through the array.
- If `nums[i] == target`, return `i`.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
