# Linked List Cycle II

## Problem Statement

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

---

## Example

**Input:**  
`head = [3,2,0,-4], pos = 1`  
**Output:**  
`Reference to node with value 2`

---

## Constraints

- The number of nodes in the list is in the range `[0, 10^4]`
- `-10^5 <= Node.val <= 10^5`

---

## Approach

- Use Floyd’s Tortoise and Hare algorithm to detect the cycle.
- Once detected, reset one pointer to head and move both at the same pace until they meet again.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
