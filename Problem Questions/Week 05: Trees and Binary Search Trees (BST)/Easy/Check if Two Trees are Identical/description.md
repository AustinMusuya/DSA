# Identical Binary Trees

## Problem Statement

Given the roots of two binary trees `root1` and `root2`, write a function to check if the two trees are identical or not. Two binary trees are identical if they are structurally identical and the nodes have the same value.

---

## Example

**Input:**  
`root1 = [1,2,3], root2 = [1,2,3]`  
**Output:**  
`true`

**Input:**  
`root1 = [1,2], root2 = [1,null,2]`  
**Output:**  
`false`

---

## Constraints

- The number of nodes in both trees is in the range `[0, 1000]`.
- `-10^5 <= Node.val <= 10^5`

---

## Approach

- Use a recursive approach to traverse both trees simultaneously.
- For each node, check if their values are equal and recurse on left and right subtrees.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h) (for recursion stack, where h is the height of the tree)
