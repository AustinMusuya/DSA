# Generate Parentheses

## Problem Statement

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

---

## Example

**Input:**  
`n = 3`  
**Output:**  
`["((()))", "(()())", "(())()", "()(())", "()()()"]`

---

## Constraints

- `1 <= n <= 8`

---

## Approach

- Use backtracking to build strings of `(` and `)` while maintaining validity.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(2^n) for generating combinations
- **Space Complexity:** O(n) per recursive call stack
