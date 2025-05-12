# Next Greater Element

## Problem Statement

Given an array `nums` of size `n`, find the next greater element for every element. The next greater element for an element `x` is the first greater element on the right side of `x` in the array. If no such element exists, set it to `-1`.

---

## Example

**Input:**  
`nums = [4, 5, 2, 25]`  
**Output:**  
`[5, 25, 25, -1]`

**Input:**  
`nums = [13, 7, 6, 12]`  
**Output:**  
`[-1, 12, 12, -1]`

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

- Use a monotonic stack to keep track of elements in decreasing order.
- Iterate from right to left.
- For each element, pop from the stack until the top is greater.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
