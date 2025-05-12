# Valid Parentheses

## Problem Statement

Given a string s containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

---

## Example

**Input:**  
`s = "{[()]}"`  
**Output:**  
`true`

---

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists only of parentheses characters.

---

## Approach

- Use a stack to push opening brackets.
- For closing brackets, pop and match from the stack.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
