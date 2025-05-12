# Min Stack

## Problem Statement

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

- `push(x)` – Push element x onto stack.
- `pop()` – Removes the element on top of the stack.
- `top()` – Get the top element.
- `getMin()` – Retrieve the minimum element in the stack.

---

## Example

**Input:**  
`push(-2), push(0), push(-3), getMin(), pop(), top(), getMin()`  
**Output:**  
`-3, 0, -2`

---

## Constraints

- All operations must be O(1).
- `-2^31 <= x <= 2^31 - 1`
- At most 3 \* 10^4 operations.

---

## Approach

- Use two stacks: one for values and one for the current minimums.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(1) per operation
- **Space Complexity:** O(n)
