# Count Unique Binary Search Trees

## Problem Statement

Given `n`, the number of nodes, return the number of structurally unique binary search trees (BSTs) that can be built with `n` nodes.

---

## Example

**Input:**  
`n = 3`  
**Output:**  
`5`  
**Explanation:**  
There are 5 unique BSTs:

```code

1         3     3      2      1
 \       /     /      / \      \
  3     2     1      1   3      2
 /     /       \                   \
2     1         2                   3
```

## Constraints

- `1 <= n <= 19`

---

## Approach

- Use dynamic programming (DP) to find the number of unique BSTs. Let `dp[i]` represent the number of unique BSTs that can be made with `i` nodes.
- For each node `i`, consider it as the root and calculate the number of BSTs formed by the left and right subtrees.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n^2), where n is the number of nodes.
- **Space Complexity:** O(n), where n is the number of nodes.
