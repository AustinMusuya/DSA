# Rotate Array by K Steps

## Problem Statement

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

You must do this **in-place**, with O(1) extra space.

---

## Example

**Input:**  
`nums = [1, 2, 3, 4, 5, 6, 7], k = 3`

**Output:**  
`[5, 6, 7, 1, 2, 3, 4]`

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

---

## Approach

- Reverse the entire array.
- Reverse the first `k` elements.
- Reverse the remaining `n - k` elements.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
