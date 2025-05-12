# Reverse a String

## Problem

Write a function that takes a string as input and returns the string reversed.

## Example

**Input:**  
`"Hi I am Austin and I rule baby!"`

**Output:**  
`"!ybab elur I dna nitsuA ma I iH"`

## Constraints

- The input string can contain spaces, punctuation, and alphabetic characters.
- 1 ≤ string.length ≤ 10^5

## Approach

- Loop from the end of the string to the beginning.
- Append characters one by one into a new string.
- Return the reversed string.

## Desired Time & Space Complexity

- **Time Complexity:** O(n)  
  You must visit each character once to reverse the string, so linear time is optimal.

- **Space Complexity:** O(n)  
  You’ll need to store a new reversed string unless doing in-place character swapping on a mutable array (not applicable for JS strings, which are immutable).
