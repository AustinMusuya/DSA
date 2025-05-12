# Linked List Cycle

## Problem Statement

Given `head`, the head of a linked list, determine if the linked list has a **cycle** in it.

A cycle occurs when a node’s `next` pointer points to a previous node in the list.

Return `true` if there is a cycle, otherwise return `false`.

---

## Example

**Input:**  
`head = [3,2,0,-4], pos = 1`

**Output:**  
`true`  
**Explanation:** There is a cycle at node with value 2.

---

## Constraints

- The number of nodes in the list is in the range `[0, 10^4]`
- `-10^5 <= Node.val <= 10^5`

---

## Approach

- Use Floyd’s Cycle Detection Algorithm (Tortoise and Hare).
- If slow and fast pointers meet, a cycle exists.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
