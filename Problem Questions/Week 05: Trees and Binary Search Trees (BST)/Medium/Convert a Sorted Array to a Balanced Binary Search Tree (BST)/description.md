# Convert Sorted Array to Balanced Binary Search Tree

## Problem Statement

Given an integer array `nums` where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

---

## Example

**Input:**  
`nums = [-10,-3,0,5,9]`  
**Output:**  
`[0,-3,9,-10,null,5]`

---

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-10^4 <= nums[i] <= 10^4`

---

## Approach

- Use the middle element of the array as the root node.
- Recursively apply the same approach to the left and right halves of the array.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(h) (for recursion stack, where h is the height of the tree)
