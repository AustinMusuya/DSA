# Design Circular Queue

## Problem Statement

Design your implementation of a circular queue. Implement the `MyCircularQueue` class:

- `MyCircularQueue(k)`: Constructor, set the size of the queue.
- `enQueue(value)`: Insert an element.
- `deQueue()`: Delete an element.
- `Front()`: Get the front item.
- `Rear()`: Get the last item.
- `isEmpty()`: Check if the queue is empty.
- `isFull()`: Check if the queue is full.

---

## Example

**Input:**  
`enQueue(1), enQueue(2), enQueue(3), enQueue(4), Rear(), isFull(), deQueue(), enQueue(4), Rear()`  
**Output:**  
`true, 3, true, true, 4`

---

## Constraints

- `1 <= k <= 1000`
- All values within signed 32-bit integer range.

---

## Approach

- Use an array with front and rear pointers.
- Use modulo arithmetic to wrap around the index.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(1) per operation
- **Space Complexity:** O(k)
