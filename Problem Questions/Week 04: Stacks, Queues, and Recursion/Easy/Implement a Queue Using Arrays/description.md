# Implement Queue Using Array

## Problem Statement

Design a queue using an array. Implement the following operations:

- `enqueue(x)`: Add element x to the end of the queue.
- `dequeue()`: Remove the element from the front of the queue.
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

- The number of operations won't exceed 10^4.
- Only use arrays and basic arithmetic.

---

## Approach

- Use a circular buffer logic or shift elements when dequeuing (tradeoff: O(n) dequeue if shifting).

---

## Desired Time & Space Complexity

- **Time Complexity:** O(1) for enqueue, O(1) average for dequeue (with circular array)
- **Space Complexity:** O(n)
