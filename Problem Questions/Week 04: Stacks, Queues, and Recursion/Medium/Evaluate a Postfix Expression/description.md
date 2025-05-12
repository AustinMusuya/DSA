# Evaluate Reverse Polish Notation

## Problem Statement

Evaluate the value of an arithmetic expression in Reverse Polish Notation (postfix). Valid operators are `+`, `-`, `*`, and `/`.

Each operand may be an integer or another expression.

---

## Example

**Input:**  
`tokens = ["2", "1", "+", "3", "*"]`  
**Output:**  
`9`  
**Explanation:** ((2 + 1) \* 3) = 9

---

## Constraints

- `1 <= tokens.length <= 10^4`
- Each token is either an operator or a number.

---

## Approach

- Use a stack to push operands.
- When an operator is encountered, pop two values and evaluate.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
