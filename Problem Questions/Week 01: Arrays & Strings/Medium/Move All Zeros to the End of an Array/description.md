# Move All Zeros to End

## Problem Statement

Given an array `nums`, move all zeros to the end of the array while maintaining the **relative order** of the non-zero elements.

Do this **in-place** without making a copy of the array.

---

## Example

**Input:**  
`nums = [0, 1, 0, 3, 12]`

**Output:**  
`[1, 3, 12, 0, 0]`

---

## Constraints

- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

---

## Approach

- Use a pointer to track position of next non-zero.
- Iterate through the array and move all non-zeros to the front.
- Fill the remaining positions with zeros.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
