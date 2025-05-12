# Tower of Hanoi

## Problem Statement

Given `n` disks stacked in ascending order of size on a source rod, move them to a destination rod using an auxiliary rod following these rules:

1. Only one disk can be moved at a time.
2. Each move involves taking the top disk from one rod and placing it on another rod.
3. No disk may be placed on top of a smaller disk.

Return the sequence of moves.

---

## Example

**Input:**  
`n = 2`  
**Output:**  
`Move disk 1 from A to B`  
`Move disk 2 from A to C`  
`Move disk 1 from B to C`

---

## Constraints

- `1 <= n <= 20`

---

## Approach

- Use recursion to solve the problem:
  - Move `n-1` disks from source to auxiliary.
  - Move last disk to destination.
  - Move `n-1` disks from auxiliary to destination.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(2^n)
- **Space Complexity:** O(n) (recursion stack)
