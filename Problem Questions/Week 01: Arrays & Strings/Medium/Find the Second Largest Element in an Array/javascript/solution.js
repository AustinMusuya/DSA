/*
# Second Largest Element in Array

## Problem Statement

Given an array of integers, find the **second largest distinct element** in the array.

If no such element exists, return an appropriate sentinel value (e.g., `-1` or `null`).

---

## Example

**Input:**  
`nums = [12, 35, 1, 10, 34, 1]`

**Output:**  
`34`

---

## Constraints

- `2 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Approach

- Initialize `max` and `secondMax`.
- Iterate through the array, updating both as needed, while skipping duplicates.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

*/

// Here we find the max value first, then find the second max value.
// which will be the value thats the largest, but not larger than the max

const secondLargest = (array) => {
  //edge cases: array has one element or is empty
  if (array.length < 2) {
    return -1;
  }

  // First, find the max value
  let maxVal = 0;
  for (i = 1; i < array.length; i++) {
    if (array[i] > array[maxVal]) {
      maxVal = i;
    }
  }
  const maxValue = array[maxVal]; //our maximum value

  //Next, find the second max value

  let secondMaxVal = null;

  for (i = 0; i < array.length; i++) {
    //check if current element is not equal to the max value
    if (array[i] != maxValue) {
      // we update the value of secondMaxVal to current if it is still null
      // or if the current element is greater
      if (secondMaxVal == null || array[i] > secondMaxVal) {
        secondMaxVal = array[i];
      }
    }
  }

  return secondMaxVal != null ? secondMaxVal : -1; //ternary expression for readability
};

console.log(secondLargest([12, 35, 1, 10, 34, 1]));
console.log(secondLargest([3, 3, 3, 3]));
console.log(secondLargest([]));
console.log(secondLargest([38]));
