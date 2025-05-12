# Find the Middle of the Linked List

## Problem Statement

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the **second** middle node.

---

## Example

**Input:**  
`head = [1, 2, 3, 4, 5]`

**Output:**  
`3`

**Input:**  
`head = [1, 2, 3, 4, 5, 6]`

**Output:**  
`4`

---

## Constraints

- The number of nodes in the list is in the range `[1, 100]`
- `1 <= Node.val <= 100`

---

## Approach

- Use two pointers: slow and fast.
- Move fast by two steps and slow by one. When fast reaches the end, slow is at the middle.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
