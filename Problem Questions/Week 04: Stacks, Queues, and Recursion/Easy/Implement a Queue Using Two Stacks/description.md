# Implement Queue Using Two Stacks

## Problem Statement

Implement a queue using two stacks. Your implementation should support:

- `enqueue(x)`: Push element x to the back of queue.
- `dequeue()`: Removes the element from in front of queue.
- `peek()`: Get the front element.
- `isEmpty()`: Returns whether the queue is empty.

---

## Example

**Input:**  
`enqueue(1), enqueue(2), peek(), dequeue(), isEmpty()`  
**Output:**  
`1, 1, true`

---

## Constraints

- Only standard stack operations are allowed.
- All operations should be amortized O(1) time.

---

## Approach

- Use one stack for input and one for output.
- Transfer elements lazily only when output stack is empty.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(1) amortized per operation
- **Space Complexity:** O(n)
