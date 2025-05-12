# Validate Binary Search Tree

## Problem Statement

Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

---

## Example

**Input:**  
`root = [2,1,3]`  
**Output:**  
`true`

**Input:**  
`root = [5,1,4,null,null,3,6]`  
**Output:**  
`false`  
**Explanation:** The root node's value is 5 but its right child's value is 4.

---

## Constraints

- The number of nodes in the tree is in the range `[1, 10^5]`.
- `-2^31 <= Node.val <= 2^31 - 1`

---

## Approach

- Perform a DFS traversal while keeping track of the valid range for each node.
- If any node violates the BST properties, return false.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h) (for recursion stack, where h is the height of the tree)
