# Palindrome Linked List

## Problem Statement

Given the head of a singly linked list, return `true` if it is a palindrome, or `false` otherwise.

---

## Example

**Input:**  
`head = [1,2,2,1]`  
**Output:**  
`true`

---

## Constraints

- The number of nodes in the list is in the range `[1, 10^5]`
- `0 <= Node.val <= 9`

---

## Approach

- Use slow and fast pointers to find the middle.
- Reverse the second half and compare it to the first half.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1) (if reversed in place)
