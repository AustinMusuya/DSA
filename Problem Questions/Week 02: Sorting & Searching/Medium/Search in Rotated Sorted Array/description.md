# Search in Rotated Sorted Array

## Problem Statement

You are given a **rotated sorted array** `nums` and an integer `target`.

Return the **index** of `target` if it is in `nums`, otherwise return `-1`.

---

## Example

**Input:**  
`nums = [4,5,6,7,0,1,2], target = 0`

**Output:**  
`4`

---

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i], target <= 10^4`
- `nums` contains **distinct values**
- `nums` is a rotation of a sorted array

---

## Approach

- Use a modified binary search to account for the rotation and decide which side is sorted.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
