# Merge Sort

## Problem Statement

Implement the **Merge Sort** algorithm to sort an array `nums` in ascending order.

Return the sorted array.

---

## Example

**Input:**  
`nums = [38, 27, 43, 3, 9, 82, 10]`

**Output:**  
`[3, 9, 10, 27, 38, 43, 82]`

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

- Divide the array into halves recursively.
- Merge sorted halves using a two-pointer technique.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
