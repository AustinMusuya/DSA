# Kth Smallest Element in a Binary Search Tree

## Problem Statement

Given the root of a binary search tree, and an integer `k`, return the `k`th smallest value (1-indexed) of all the nodes in the tree.

---

## Example

**Input:**  
`root = [3,1,4,null,2], k = 1`  
**Output:**  
`1`

**Input:**  
`root = [5,3,6,2,4,null,null,1], k = 3`  
**Output:**  
`3`

---

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-10^4 <= Node.val <= 10^4`

---

## Approach

- Perform an inorder traversal, as this will give the nodes in ascending order.
- Track the count of nodes visited and return the `k`th smallest node.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h) (for recursion stack, where h is the height of the tree)
