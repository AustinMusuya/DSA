# Largest Rectangle in Histogram

## Problem Statement

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

---

## Example

**Input:**  
`heights = [2,1,5,6,2,3]`  
**Output:**  
`10`  
**Explanation:** Rectangle of height 5 and 6 with width 2.

---

## Constraints

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

---

## Approach

- Use a monotonic increasing stack to keep track of bar indices.
- Calculate max area by popping when the current height is less than the top of the stack.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
