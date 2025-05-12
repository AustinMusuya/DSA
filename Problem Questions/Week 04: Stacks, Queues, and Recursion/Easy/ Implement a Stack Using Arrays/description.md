# Implement Stack Using Array

## Problem Statement

Design a stack data structure using arrays. Implement the following operations:

- `push(x)`: Insert element x onto stack.
- `pop()`: Removes the element on top of the stack.
- `top()`: Get the top element.
- `isEmpty()`: Returns whether the stack is empty.

---

## Example

**Input:**  
`push(1), push(2), top(), pop(), isEmpty()`  
**Output:**  
`2, 2, true`

---

## Constraints

- All operations must run in O(1) time.
- The number of calls won't exceed 10^4.

---

## Approach

- Use a dynamic array to simulate stack behavior.
- Track top index manually.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(1) per operation
- **Space Complexity:** O(n) where n is the number of elements
