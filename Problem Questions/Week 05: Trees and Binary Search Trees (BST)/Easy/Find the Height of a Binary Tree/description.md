# Height of Binary Tree

## Problem Statement

Given the root of a binary tree, return its height. The height of a binary tree is the number of edges along the longest path from the root node to any leaf node.

---

## Example

**Input:**  
`root = [3,9,20,null,null,15,7]`  
**Output:**  
`3`  
**Explanation:** The height of the tree is 3.

---

## Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

---

## Approach

- Use a recursive DFS approach to traverse the tree.
- For each node, calculate the height of its left and right subtrees.
- The height of the node is `1 + max(left height, right height)`.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h) (for recursion stack, where h is the height of the tree)
