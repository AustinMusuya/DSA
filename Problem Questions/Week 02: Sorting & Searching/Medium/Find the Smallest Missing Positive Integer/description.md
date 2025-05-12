# First Missing Positive

## Problem Statement

Given an unsorted integer array `nums`, find the **smallest missing positive integer**.

You must implement an algorithm that runs in **O(n)** time and uses **constant space**.

---

## Example

**Input:**  
`nums = [3, 4, -1, 1]`

**Output:**  
`2`

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

---

## Approach

- Ignore negatives and out-of-bound values.
- Use index mapping (bucket sort style) to place each number at its correct index if possible.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
