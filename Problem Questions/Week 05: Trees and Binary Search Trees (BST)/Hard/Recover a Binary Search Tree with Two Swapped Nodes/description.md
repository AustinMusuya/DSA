# Recover Binary Search Tree

## Problem Statement

Given the root of a binary search tree (BST) where two nodes have been swapped by mistake, recover the BST.

A BST is valid if for every node:

- All values in its left subtree are smaller than its value.
- All values in its right subtree are greater than its value.

Return the root of the binary search tree after recovering it.

---

## Example

**Input:**  
`root = [1,3,null,null,2]`  
**Output:**  
`[3,1,null,null,2]`

---

## Constraints

- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`

---

## Approach

- Perform an inorder traversal to identify the two nodes that are swapped.
- Once identified, swap them back to recover the BST.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n), where n is the number of nodes in the tree.
- **Space Complexity:** O(h), where h is the height of the tree (for the recursion stack).
