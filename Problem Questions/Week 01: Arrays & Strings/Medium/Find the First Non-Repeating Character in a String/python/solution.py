"""
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

"""
# Create a hashmap to store the characters.
# Loop through the array increasing the count of each character you find by 1.
# return the first character with a count of 1

# Example: 'leetcode' -> 1
# Note: space complexity is still O(1) since there are only 26 characters in alphabet.
# No matter size of input, the space in hashmap will never be more than 26 characters


def first_non_recurring(word: str) -> int:
    # edge case1: different casing in word
    word = word.lower()
    # edge cases: empty string
    if not word:
        return -1
    # hashmap
    map = {}

    # loop through the word
    for i in range(len(word)):
        if word[i] not in map:
            map[word[i]] = 1
        else:
            map[word[i]] += 1

    for i in range(len(word)):
        if map[word[i]] == 1:
            return i

    return -1


print(first_non_recurring("leetcode"))
print(first_non_recurring("Leetcode"))
print(first_non_recurring("littlecode"))
print(first_non_recurring("Littlecode"))
