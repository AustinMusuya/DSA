# Maximum Depth of Binary Tree

## Problem Statement

Given the root of a binary tree, return its maximum depth. The maximum depth of a binary tree is the number of nodes along the longest path from the root node to the farthest leaf node.

---

## Example

**Input:**  
`root = [3,9,20,null,null,15,7]`  
**Output:**  
`3`  
**Explanation:** The maximum depth of the tree is 3.

---

## Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

---

## Approach

- Use a recursive DFS approach to calculate the depth.
- The depth of a node is `1 + max(left depth, right depth)`.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h) (for recursion stack, where h is the height of the tree)
