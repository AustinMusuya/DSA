# Implement Breadth-First Search (BFS) on a Graph

## Problem Statement

Given an undirected graph represented as an adjacency list and a starting node, implement Breadth-First Search (BFS) to visit all reachable nodes from the starting point.

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

**Output:** `[0, 1, 2, 3]` (may vary based on implementation)

---

## Constraints

- 1 <= number of nodes <= 10^5
- Graph can be disconnected
- Graph is undirected and unweighted

---

## Approach

- Use a queue to explore the graph level-by-level.
- Maintain a visited set to avoid revisiting nodes.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V)
