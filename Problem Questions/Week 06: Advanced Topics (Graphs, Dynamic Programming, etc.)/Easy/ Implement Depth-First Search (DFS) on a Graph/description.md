# Implement Depth-First Search (DFS) on a Graph

## Problem Statement

Given an undirected graph represented as an adjacency list and a starting node, implement Depth-First Search (DFS) to visit all reachable nodes from the starting point.

Return the order of nodes visited.

---

## Example

**Input:**

```code
graph = {
0: [1, 2],
1: [0, 3],
2: [0],
3: [1]
}, start = 0
```

**Output:** `[0, 1, 3, 2]` (may vary based on implementation)

---

## Constraints

- 1 <= number of nodes <= 10^5
- Graph can be disconnected
- Graph is undirected and unweighted

---

## Approach

- Use a recursive or iterative stack-based approach.
- Track visited nodes to prevent cycles.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(V + E), where V = number of vertices, E = number of edges
- **Space Complexity:** O(V), for visited tracking and recursion/stack
