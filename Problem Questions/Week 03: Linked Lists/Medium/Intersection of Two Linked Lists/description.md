# Intersection of Two Linked Lists

## Problem Statement

Given the heads of two singly linked lists `headA` and `headB`, return the node at which the two lists intersect. If the two linked lists have no intersection, return `null`.

---

## Example

**Input:**  
`headA = [4,1,8,4,5], headB = [5,6,1,8,4,5]`  
**Output:**  
`Reference to node with value 8`

---

## Constraints

- The number of nodes in both lists is in the range `[0, 10^4]`
- `1 <= Node.val <= 10^5`

---

## Approach

- Use two pointers.
- Traverse both lists, and when either hits the end, move it to the head of the other list.
- If there is an intersection, they will meet; otherwise, both will be null.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n + m)
- **Space Complexity:** O(1)
