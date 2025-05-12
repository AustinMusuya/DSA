# Remove Duplicates from a Sorted Linked List

## Problem Statement

Given the `head` of a **sorted** linked list, delete all duplicates such that each element appears only once.

Return the linked list **without duplicates**.

---

## Example

**Input:**  
`head = [1, 1, 2, 3, 3]`

**Output:**  
`[1, 2, 3]`

---

## Constraints

- The number of nodes in the list is in the range `[0, 300]`
- `-100 <= Node.val <= 100`

---

## Approach

- Traverse the list with one pointer.
- If the current node’s value equals the next node’s value, skip the next node.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
