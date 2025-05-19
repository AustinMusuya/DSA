"""
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
"""

"""
//  Approach using unicode characters. T- O(n), S- O(1)

// Very smart algorithm, we start by initializing an array of size 26 with all values as 0.
// Next we loop through the length of either of the two strings,
// subtracting every character's unicode value with unicode value of 'a' (97).
// then we increament the value at that index by 1 in the first string
// and decrement the value by -1 in the second string
// finally we loop through the final array which should have all 0s if the strings are anagrams
/*

example for words "race" and "care"

Now go step-by-step:
i = 0:

    ord(s[0]) = 'r' → index 17 → count[17]++ → 1

    ord(t[0]) = 'c' → index 2 → count[2]-- → -1

i = 1:

    ord(s[1]) = 'a' → index 0 → count[0]++ → 1

    ord(t[1]) = 'a' → index 0 → count[0]-- → 0

i = 2:

    ord(s[2]) = 'c' → index 2 → count[2]++ → 0 (was -1)

    ord(t[2]) = 'r' → index 17 → count[17]-- → 0 (was 1)

i = 3:

    ord(s[3]) = 'e' → index 4 → count[4]++ → 1

    ord(t[3]) = 'e' → index 4 → count[4]-- → 0
*/
"""


def is_anagram(str1: str, str2: str) -> bool:
    # Edge case 1: handle different casing in characters
    str1 = str1.lower()
    str2 = str2.lower()
    # Edge Cae 2 : Handle different length size of characters
    if len(str1) != len(str2):
        return False

    # Lets create an empty array of 26 characters and fill it with 0
    count = [0] * 26

    # loop through the length of either of the strings and update the value at every position in count
    for i in range(len(str1)):
        count[ord(str1[i]) - ord("a")] += 1
        count[ord(str2[i]) - ord("a")] -= 1

    # check for the final characters in count array, if a position is not 0, return false

    for i in count:
        if i != 0:
            return False

    return True


print(is_anagram("race", "care"))
print(is_anagram("", "tar"))
print(is_anagram("rat", "car"))
print(is_anagram("raCe", "Care"))
print(is_anagram("", ""))
