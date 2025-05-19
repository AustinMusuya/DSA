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

// console.log(checkAnagram("rat", "tar"));
// console.log(checkAnagram("", "tar"));
// console.log(checkAnagram("rat", "car"));
// console.log(checkAnagram("race", "care"));
// console.log(checkAnagram("", ""));
// console.log(checkAnagram("", ""));

// Note: This approach gives both linear,O(n), space and time complexity.

//  Different Approach using unicode characters. T- O(n), S- O(1)

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

    s.charAt(0) = 'r' → index 17 → count[17]++ → 1

    t.charAt(0) = 'c' → index 2 → count[2]-- → -1

i = 1:

    s.charAt(1) = 'a' → index 0 → count[0]++ → 1

    t.charAt(1) = 'a' → index 0 → count[0]-- → 0

i = 2:

    s.charAt(2) = 'c' → index 2 → count[2]++ → 0 (was -1)

    t.charAt(2) = 'r' → index 17 → count[17]-- → 0 (was 1)

i = 3:

    s.charAt(3) = 'e' → index 4 → count[4]++ → 1

    t.charAt(3) = 'e' → index 4 → count[4]-- → 0
*/

const isAnagram = (string1, string2) => {
  // Edge case1: a difference in casing of characters
  string1 = string1.toLowerCase();
  string2 = string2.toLowerCase();

  // Edge case2: incase of empty string or different sizes of strings
  if (string1.length != string2.length) {
    return false;
  }

  // lets create an empty array of size 26 with 0s in each index with the Array class
  const count = new Array(26).fill(0);

  // Loop through the length of either string updating the value of 0 in the corresponding index
  for (let i = 0; i < string1.length; i++) {
    count[string1.charCodeAt[i] - "a".charCodeAt[0]]++;
    count[string2.charCodeAt[i] - "a".charCodeAt[0]]--;
  }

  for (let i = 0; i < count.length; i++) {
    if (count[i] != 0) {
      return false;
    }
  }

  return true;
};

console.log(isAnagram("race", "care"));
console.log(isAnagram("", "tar"));
console.log(isAnagram("rat", "car"));
console.log(isAnagram("raCe", "Care"));
console.log(isAnagram("", ""));
console.log(isAnagram("", ""));
