# Topological Sort

## Problem Statement

Given a directed acyclic graph (DAG), perform a topological sort of the vertices.

Return an array representing one possible topological order.

---

## Example

**Input:**

```code
graph = {
0: [1],
1: [2],
2: []
}
```

**Output:** `[0, 1, 2]`

---

## Constraints

- 1 <= number of nodes <= 10^5
- Graph must be a DAG.

---

## Approach

- Use Kahn’s algorithm (BFS + in-degree) or DFS with a stack.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V)
