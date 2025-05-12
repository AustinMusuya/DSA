# Add Two Numbers

## Problem Statement

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

---

## Example

**Input:**  
`l1 = [2,4,3], l2 = [5,6,4]`  
**Output:**  
`[7,0,8]`  
**Explanation:** 342 + 465 = 807.

---

## Constraints

- The number of nodes in each list is in the range `[1, 100]`
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a non-negative integer.

---

## Approach

- Traverse both lists.
- Maintain a carry.
- Create new nodes for each digit of the sum.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(max(n, m))
- **Space Complexity:** O(max(n, m)) (for the output list)
