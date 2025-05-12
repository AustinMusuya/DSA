# Construct Binary Tree from Inorder and Preorder Traversals

## Problem Statement

Given two integer arrays `inorder` and `preorder` where:

- `preorder` is the preorder traversal of a binary tree.
- `inorder` is the inorder traversal of the same binary tree.

Return the root of the binary tree constructed from these traversals.

---

## Example

**Input:**  
`preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]`  
**Output:**  
`[3,9,20,null,null,15,7]`

---

## Constraints

- `1 <= inorder.length <= 3000`
- `preorder.length == inorder.length`
- The values of `inorder` and `preorder` are distinct.

---

## Approach

- The first element in `preorder` is always the root of the tree.
- Find this element in the `inorder` array to divide the tree into left and right subtrees.
- Recursively repeat the process for the left and right subtrees using the remaining elements.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
