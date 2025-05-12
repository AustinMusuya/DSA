# Longest Common Subsequence (LCS)

## Problem Statement

Given two strings `text1` and `text2`, return the length of their longest common subsequence.

---

## Example

**Input:**  
`text1 = "abcde", text2 = "ace"`  
**Output:** `3`  
**Explanation:** The LCS is `"ace"`

---

## Constraints

- 1 <= text1.length, text2.length <= 1000

---

## Approach

- Use dynamic programming with a 2D table to compute LCS length.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n \* m)
- **Space Complexity:** O(n \* m) or O(min(n, m)) with optimized space
