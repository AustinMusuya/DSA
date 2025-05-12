# MinMax Stack

## Problem Statement

Design a stack that supports push, pop, top, getMin, and getMax operations in constant time.

Implement a class with the following methods:

- `push(x)`
- `pop()`
- `top()`
- `getMin()`
- `getMax()`

---

## Example

**Input:**  
`push(5), push(3), push(7), getMin(), getMax(), pop(), getMin(), getMax()`  
**Output:**  
`3, 7, 3, 5`

---

## Constraints

- `-10^9 <= x <= 10^9`
- Up to 10^5 operations.

---

## Approach

- Use an auxiliary stack to track min values.
- Use another auxiliary stack to track max values.
- Maintain these stacks alongside the main stack.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(1) per operation
- **Space Complexity:** O(n)
