# Binary Tree Traversals

## Problem Statement

Given the root of a binary tree, implement the following tree traversals:

- **Inorder Traversal:** Visit the left subtree, then the root node, and finally the right subtree.
- **Preorder Traversal:** Visit the root node, then the left subtree, and finally the right subtree.
- **Postorder Traversal:** Visit the left subtree, then the right subtree, and finally the root node.

Return the result of each traversal.

---

## Example

**Input:**  
`root = [1,null,2,3]`  
**Output:**  
`Inorder: [1,3,2]`  
`Preorder: [1,2,3]`  
`Postorder: [3,2,1]`

---

## Constraints

- The number of nodes in the tree is in the range `[0, 1000]`.
- `-100 <= Node.val <= 100`

---

## Approach

- Use recursion or iteration (stack-based) to perform each traversal.
- For **Inorder**, traverse left subtree, then root, then right subtree.
- For **Preorder**, traverse root first, then left, then right.
- For **Postorder**, traverse left, right, and then root.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h) (for recursion stack or stack-based iteration)
