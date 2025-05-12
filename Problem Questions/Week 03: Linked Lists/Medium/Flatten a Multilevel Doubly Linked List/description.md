# Flatten a Multilevel Doubly Linked List

## Problem Statement

You are given a doubly linked list, where in addition to the next and previous pointers, each node has a child pointer, which may point to a separate doubly linked list.

These child lists may also have one or more child nodes of their own, and so on.

Flatten the list so that all the nodes appear in a single-level, doubly linked list.

---

## Example

**Input:**  
`head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]`  
**Output:**  
`[1,2,3,7,8,11,12,9,10,4,5,6]`

---

## Constraints

- The number of nodes in the list is in the range `[0, 1000]`
- `-10^5 <= Node.val <= 10^5`

---

## Approach

- Use depth-first traversal.
- Flatten child nodes recursively and reconnect them with the main list.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n) (due to recursion stack)
