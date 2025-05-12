# Reverse Nodes in k-Group

## Problem Statement

Given the head of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k`, then left-out nodes should remain as is.

---

## Example

**Input:**  
`head = [1,2,3,4,5], k = 2`  
**Output:**  
`[2,1,4,3,5]`

---

## Constraints

- The number of nodes in the list is in the range `[1, 5000]`
- `0 <= Node.val <= 1000`
- `1 <= k <= 5000`

---

## Approach

- Use recursion or iteration to reverse the list in chunks of size `k`.
- Connect the reversed sublists together.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n/k) for recursion or O(1) for iterative in-place
