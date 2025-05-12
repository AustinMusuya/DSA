# Merge Two Sorted Linked Lists

## Problem Statement

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a sorted manner and return the merged list.

---

## Example

**Input:**  
`list1 = [1, 2, 4]`  
`list2 = [1, 3, 4]`

**Output:**  
`[1, 1, 2, 3, 4, 4]`

---

## Constraints

- The number of nodes in both lists is in the range `[0, 50]`
- `-100 <= Node.val <= 100`

---

## Approach

- Use two pointers to iterate through both lists.
- Compare values and build a new list or modify one of the existing lists in-place.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n + m)
- **Space Complexity:** O(1) if done in-place, else O(n + m)
