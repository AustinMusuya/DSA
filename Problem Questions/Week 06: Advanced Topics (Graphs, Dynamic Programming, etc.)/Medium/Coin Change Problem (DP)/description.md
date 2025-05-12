# Coin Change

## Problem Statement

You are given coins of different denominations and a total amount. Return the fewest number of coins needed to make up that amount. If it is not possible, return -1.

---

## Example

**Input:** `coins = [1, 2, 5], amount = 11`  
**Output:** `3`  
**Explanation:** 11 = 5 + 5 + 1

---

## Constraints

- 1 <= coins.length <= 12
- 0 <= amount <= 10^4
- All coin values are positive integers

---

## Approach

- Use bottom-up dynamic programming to build the minimum number of coins for each amount.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(amount \* coins.length)
- **Space Complexity:** O(amount)
