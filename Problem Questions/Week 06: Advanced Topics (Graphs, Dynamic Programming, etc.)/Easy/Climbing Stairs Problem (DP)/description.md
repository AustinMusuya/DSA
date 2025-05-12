# Climbing Stairs

## Problem Statement

You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps.

In how many distinct ways can you climb to the top?

---

## Example

**Input:** `n = 5`  
**Output:** `8`

---

## Constraints

- 1 <= n <= 45

---

## Approach

- This is a variation of the Fibonacci problem.
- Use bottom-up DP to store number of ways to reach each step.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1) with optimized space, O(n) with full DP array
