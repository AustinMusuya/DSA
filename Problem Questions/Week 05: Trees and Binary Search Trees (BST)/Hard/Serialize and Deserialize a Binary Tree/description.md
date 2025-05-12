# Serialize and Deserialize Binary Tree

## Problem Statement

Design an algorithm to serialize and deserialize a binary tree. Serialization is the process of converting a binary tree into a string, and deserialization is the process of converting the string back to a binary tree.

Implement the `Codec` class:

- `Codec.serialize(root)` serializes the tree to a string.
- `Codec.deserialize(data)` deserializes the string back to the original tree.

---

## Example

**Input:**  
`root = [1,2,3,null,null,4,5]`  
**Output:**  
`["1","2","3","null","null","4","5"]`

---

## Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-1000 <= Node.val <= 1000`

---

## Approach

- Use a recursive DFS approach to traverse the tree and convert each node to a string.
- For deserialization, use a queue to reconstruct the tree from the string.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n), where n is the number of nodes in the tree.
- **Space Complexity:** O(n), due to the storage required for serialization and deserialization.
