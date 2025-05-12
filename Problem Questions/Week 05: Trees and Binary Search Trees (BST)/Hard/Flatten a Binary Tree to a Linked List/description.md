# Flatten Binary Tree to Linked List

## Problem Statement

Given a binary tree, flatten it to a linked list in-place.

For example:

```code
Given:
1
/
2 5
/ \
3 4 6
```

The flattened tree should look like:
1 -> 2 -> 3 -> 4 -> 5 -> 6

## Example

**Input:**  
`root = [1,2,5,3,4,null,6]`  
**Output:**  
`[1,null,2,null,3,null,4,null,5,null,6]`

---

## Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-100 <= Node.val <= 100`

---

## Approach

- Perform a DFS or preorder traversal of the tree.
- Flatten the left and right subtrees first, and then modify the current node to point to the left flattened subtree.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n), where n is the number of nodes in the tree.
- **Space Complexity:** O(h), where h is the height of the tree (for the recursion stack).
