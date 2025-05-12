# Reverse an Array

## Problem Statement

Given an array of integers, return the array with elements in **reverse order**.

---

## Example

**Input:**  
`nums = [1, 2, 3, 4, 5]`

**Output:**  
`[5, 4, 3, 2, 1]`

---

## Constraints

- `1 <= nums.length <= 10^5`

---

## Approach

- Use two pointers (`left` and `right`) to swap values from the ends toward the center.
- In-place swap until `left >= right`.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1) (in-place reversal)
