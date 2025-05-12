# Detect a Cycle in a Directed Graph

## Problem Statement

Given a directed graph, determine if it contains a cycle.

Return `true` if there is at least one cycle, otherwise return `false`.

---

## Example

**Input:**

```code
graph = {
0: [1],
1: [2],
2: [0]
}
```

**Output:** `true`

---

## Constraints

- 1 <= number of nodes <= 10^5
- Graph is represented as an adjacency list.

---

## Approach

- Use Depth-First Search (DFS) with a recursion stack.
- Keep track of visited nodes and the current path to detect cycles.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V)
