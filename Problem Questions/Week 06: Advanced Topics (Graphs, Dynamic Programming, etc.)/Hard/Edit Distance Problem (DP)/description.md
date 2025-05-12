# Edit Distance (Levenshtein Distance)

## Problem Statement

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

Allowed operations: insert, delete, replace a character.

---

## Example

**Input:**  
`word1 = "horse", word2 = "ros"`  
**Output:** `3`  
**Explanation:** horse -> rorse (replace) -> rose (delete) -> ros (delete)

---

## Constraints

- 1 <= word1.length, word2.length <= 500

---

## Approach

- Use DP with a 2D table where dp[i][j] stores min operations to convert first i characters of word1 to first j of word2.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n \* m)
- **Space Complexity:** O(n \* m)
