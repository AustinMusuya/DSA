# Reverse a Linked List

## Problem Statement

Given the `head` of a singly linked list, reverse the list and return the new head.

---

## Example

**Input:**  
`head = [1, 2, 3, 4, 5]`

**Output:**  
`[5, 4, 3, 2, 1]`

---

## Constraints

- The number of nodes in the list is in the range `[0, 5000]`
- `-5000 <= Node.val <= 5000`

---

## Approach

- Use an iterative approach with three pointers: `prev`, `current`, and `next`.
- Rewire the `next` pointers as you traverse the list.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
