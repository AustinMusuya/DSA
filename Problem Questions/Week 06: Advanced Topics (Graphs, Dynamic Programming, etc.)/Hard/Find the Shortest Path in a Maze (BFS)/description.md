# Shortest Path in a Maze (BFS)

## Problem Statement

Given a 2D maze with walls and open paths, find the shortest path from the start to the destination.

Return the minimum number of steps, or -1 if the path doesn’t exist.

---

## Example

**Input:**

```code
maze = [
[0, 0, 1, 0],
[1, 0, 1, 0],
[0, 0, 0, 0],
[1, 1, 1, 0]
]
start = (0, 0)
end = (2, 3)
```

**Output:** `5`

---

## Constraints

- Maze size up to 10^3 x 10^3
- 0 = path, 1 = wall

---

## Approach

- Perform BFS from the start position.
- Use a queue to explore neighbors and a visited set to avoid revisiting.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(N \* M)
- **Space Complexity:** O(N \* M)
