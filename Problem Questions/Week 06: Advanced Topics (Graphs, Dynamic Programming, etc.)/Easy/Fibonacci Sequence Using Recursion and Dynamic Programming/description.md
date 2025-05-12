# Fibonacci Number

## Problem Statement

The Fibonacci numbers are defined as:

- `F(0) = 0`, `F(1) = 1`
- `F(n) = F(n - 1) + F(n - 2)` for n > 1

Write a function to return the `n-th` Fibonacci number.

---

## Example

**Input:** `n = 6`  
**Output:** `8`

---

## Constraints

- 0 <= n <= 30 (recursive)
- 0 <= n <= 10^5 (DP approach)

---

## Approach

- Use a recursive approach for small `n`.
- For large `n`, use bottom-up dynamic programming to avoid repeated calculations.

---

## Desired Time & Space Complexity

- **Recursive Time Complexity:** O(2^n)
- **DP Time Complexity:** O(n), Space: O(1) or O(n)
