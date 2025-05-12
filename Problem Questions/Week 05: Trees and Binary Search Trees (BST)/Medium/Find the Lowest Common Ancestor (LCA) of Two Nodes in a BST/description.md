# Lowest Common Ancestor of a Binary Search Tree

## Problem Statement

Given the root of a binary search tree (BST) and two nodes `p` and `q`, return the lowest common ancestor (LCA) of the two nodes.

The LCA of two nodes `p` and `q` in a BST is defined as the lowest node in the tree that has both `p` and `q` as descendants (where a node can be a descendant of itself).

---

## Example

**Input:**  
`root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8`  
**Output:**  
`6`  
**Explanation:** The LCA of nodes 2 and 8 is 6.

---

## Constraints

- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are unique.

---

## Approach

- Starting from the root, if both `p` and `q` are smaller than the root, move to the left subtree.
- If both `p` and `q` are greater than the root, move to the right subtree.
- If one of `p` or `q` is smaller and the other is larger, the root is their LCA.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(h) where h is the height of the tree
- **Space Complexity:** O(1) (no extra space needed)
