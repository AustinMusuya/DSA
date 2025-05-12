# First Non-Repeating Character in String

## Problem Statement

Given a string `s`, return the **index** of the first non-repeating character.

If it doesn't exist, return `-1`.

---

## Example

**Input:**  
`s = "leetcode"`  
**Output:**  
`0`

**Input:**  
`s = "aabb"`  
**Output:**  
`-1`

---

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.

---

## Approach

- Count frequency of each character using a hash map.
- Iterate through the string again to find the first character with a count of 1.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1) — 26 letters in lowercase alphabet
