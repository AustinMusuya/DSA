# Trapping Rain Water

## Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute **how much water it can trap** after raining.

---

## Example

**Input:**  
`height = [0,1,0,2,1,0,1,3,2,1,2,1]`

**Output:**  
`6`

---

## Constraints

- `1 <= height.length <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

---

## Approach

- Use two-pointer approach:
  - Track left and right max heights as you move inward.
  - Accumulate trapped water based on shorter side.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
