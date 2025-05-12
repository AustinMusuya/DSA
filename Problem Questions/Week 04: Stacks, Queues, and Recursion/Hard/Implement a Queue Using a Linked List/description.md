# Queue Using Linked List

## Problem Statement

Implement a queue using a singly or doubly linked list with standard operations:

- `enqueue(x)`: Add an element to the rear of the queue.
- `dequeue()`: Remove and return the front element.
- `peek()`: Return the front element without removing it.
- `isEmpty()`: Return whether the queue is empty.

---

## Example

**Input:**  
`enqueue(10), enqueue(20), dequeue(), peek()`  
**Output:**  
`10, 20`

---

## Constraints

- You may assume standard linked list node structure.

---

## Approach

- Maintain head and tail pointers.
- Ensure constant time operations using pointers.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(1) per operation
- **Space Complexity:** O(n)
