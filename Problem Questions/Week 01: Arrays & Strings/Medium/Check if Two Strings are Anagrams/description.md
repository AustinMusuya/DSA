# Valid Anagram

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of another, using **all the original letters exactly once**.

---

## Example

**Input:**  
`s = "anagram", t = "nagaram"`  
**Output:**  
`true`

**Input:**  
`s = "rat", t = "car"`  
**Output:**  
`false`

---

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

---

## Approach

- Count the characters in both strings using frequency maps (or arrays).
- Compare the counts.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1) — alphabet size is constant
