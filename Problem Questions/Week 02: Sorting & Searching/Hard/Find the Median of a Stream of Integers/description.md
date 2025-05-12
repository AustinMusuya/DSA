# Median from Data Stream

## Problem Statement

Design a data structure that supports:

- `addNum(num)`: Adds a number to the stream.
- `findMedian()`: Returns the **median** of all numbers added so far.

---

## Example

**Input:**  
`addNum(1)`  
`addNum(2)`  
`findMedian()` → 1.5  
`addNum(3)`  
`findMedian()` → 2

---

## Constraints

- You must implement `addNum` in O(log n) time and `findMedian` in O(1) time.
- All values are integers between `-10^5` and `10^5`.

---

## Approach

- Use two heaps: max-heap for lower half and min-heap for upper half.
- Balance the heaps to ensure size difference is ≤ 1.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(log n) for add, O(1) for find
- **Space Complexity:** O(n)
