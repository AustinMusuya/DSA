# Remove Nth Node From End of List

## Problem Statement

Given the head of a linked list, remove the nth node from the end of the list and return its head.

---

## Example

**Input:**  
`head = [1,2,3,4,5], n = 2`  
**Output:**  
`[1,2,3,5]`

---

## Constraints

- The number of nodes in the list is `sz`
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

---

## Approach

- Use a two-pointer technique: advance one pointer `n` steps ahead.
- Move both pointers until the first one hits the end.
- The second pointer will be right before the node to remove.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
