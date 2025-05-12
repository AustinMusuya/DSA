# Square Root Using Binary Search

## Problem Statement

Given a non-negative integer `x`, compute and return the **square root** of `x`.

Only the **integer part** of the square root should be returned.

---

## Example

**Input:**  
`x = 8`

**Output:**  
`2`  
**Explanation:** The square root of 8 is approximately 2.82842, and the integer part is 2.

---

## Constraints

- `0 <= x <= 2^31 - 1`

---

## Approach

- Use binary search between 0 and x to find the greatest `mid` such that `mid * mid <= x`.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(log x)
- **Space Complexity:** O(1)
