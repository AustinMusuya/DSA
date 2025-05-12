# Diameter of Binary Tree

## Problem Statement

Given the root of a binary tree, return the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

---

## Example

**Input:**  
`root = [1,2,3,4,5]`  
**Output:**  
`3`  
**Explanation:** The longest path is between nodes 4 and 5, which has a length of 3.

---

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`

---

## Approach

- Perform a DFS traversal of the tree to find the longest path between any two nodes.
- At each node, calculate the depth of the left and right subtrees. The diameter at that node is the sum of the depths of the left and right subtrees.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n), where n is the number of nodes in the tree.
- **Space Complexity:** O(h), where h is the height of the tree (for the recursion stack).
