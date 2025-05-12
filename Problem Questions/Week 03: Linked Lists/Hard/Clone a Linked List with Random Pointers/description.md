# Copy List with Random Pointer

## Problem Statement

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

---

## Example

**Input:**  
`head = [[7,null],[13,0],[11,4],[10,2],[1,0]]`  
**Output:**  
A deep copy with same structure and values

---

## Constraints

- The number of nodes in the list is in the range `[0, 1000]`
- `-10000 <= Node.val <= 10000`
- `Node.random` is null or points to a node in the list

---

## Approach

- First pass: Create a mapping from old nodes to new nodes.
- Second pass: Assign next and random pointers using the map.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
