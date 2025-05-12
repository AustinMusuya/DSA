# Dijkstra’s Algorithm for Shortest Path

## Problem Statement

Given a weighted graph and a source vertex, find the shortest path from the source to all other vertices in the graph.

Return an array of shortest distances from the source to each vertex.

---

## Example

**Input:**

```code
graph = {
0: [(1, 2), (2, 4)],
1: [(2, 1)],
2: []
}
source = 0
```

**Output:** `[0, 2, 3]`

---

## Constraints

- 1 <= number of nodes <= 10^5
- Edges are non-negative weights

---

## Approach

- Use a priority queue (min-heap) to greedily pick the minimum distance vertex.
- Track the shortest distances in a dictionary or array.

---

## Desired Time & Space Complexity

- **Time Complexity:** O((V + E) log V)
- **Space Complexity:** O(V)
