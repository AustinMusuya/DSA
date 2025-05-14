/*
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
*/

// To check that a word is an anagram of another, both inputs need to be of the same length
// in character and have the same character type count.
// We can try store the count of the first input in a hashmap
// and compare each of that to the second input.

const checkAnagram = (input1, input2) => {
  // edge cases:Empty value in one of the inputs.
  // Check if the character count in both inputs do not match
  if (!input1 || !input2 || input1.length != input2.length) {
    return false;
  }
  let freq = {}; //keep track of the frequency of characters

  for (let i = 0; i < input1.length; i++) {
    const char = input1[i];
    if (!freq[char]) {
      freq[char] = 1;
    } else {
      freq[char] = freq[char] + 1;
    }
  }
  for (let i = 0; i < input2.length; i++) {
    const char = input2[i];
    if (!freq[char]) {
      return false; // char not found or overused
    }
    freq[char]--;
  }
  return true;
};

console.log(checkAnagram("rat", "tar"));
console.log(checkAnagram("", "tar"));
console.log(checkAnagram("rat", "car"));
console.log(checkAnagram("race", "care"));
console.log(checkAnagram("", ""));
console.log(checkAnagram("", ""));

// Note: This approach gives both linear,O(n), space and time complexity.
