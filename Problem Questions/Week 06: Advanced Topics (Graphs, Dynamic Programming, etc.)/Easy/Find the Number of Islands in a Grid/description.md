# Number of Islands

## Problem Statement

Given a 2D grid of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

---

## Example

**Input:**

```code
grid = [
["1","1","0","0"],
["1","0","0","1"],
["0","0","1","1"],
["0","0","0","0"]
]
```

**Output:** `3`

## Constraints

- 1 <= grid.length, grid[0].length <= 300

---

## Approach

- Traverse the grid using DFS or BFS.
- Whenever a `'1'` is found, initiate a traversal to mark all connected land as visited.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(m \* n)
- **Space Complexity:** O(m \* n) for visited or recursion
