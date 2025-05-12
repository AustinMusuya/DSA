# Symmetric Binary Tree

## Problem Statement

Given the root of a binary tree, check whether the tree is symmetric around its center. A tree is symmetric if the left and right subtrees are mirror images of each other.

---

## Example

**Input:**  
`root = [1,2,2,3,4,4,3]`  
**Output:**  
`true`

**Input:**  
`root = [1,2,2,null,3,null,3]`  
**Output:**  
`false`

---

## Constraints

- The number of nodes in the tree is in the range `[0, 1000]`.
- `-100 <= Node.val <= 100`

---

## Approach

- Use a recursive approach to compare the left and right subtrees.
- At each step, check if the values of the nodes are equal and recursively check their subtrees for symmetry.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h) (for recursion stack, where h is the height of the tree)
