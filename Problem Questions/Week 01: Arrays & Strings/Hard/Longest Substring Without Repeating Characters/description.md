# Longest Substring Without Repeating Characters

## Problem Statement

Given a string `s`, find the length of the **longest substring** without repeating characters.

---

## Example

**Input:**  
`s = "abcabcbb"`

**Output:**  
`3`  
**Explanation:** The answer is `"abc"`, with length 3.

---

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

---

## Approach

- Use sliding window with a set to track characters.
- Expand the window until a duplicate is found.
- Shrink window from the left until the substring is valid again.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(min(n, m)) — where `m` is the character set size
