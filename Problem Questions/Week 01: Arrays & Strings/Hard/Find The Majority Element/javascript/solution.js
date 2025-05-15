/*
# Majority Element

## Problem Statement

Given an array `nums` of size `n`, return the **majority element**. The majority element is the element that appears **more than ⌊n / 2⌋ times**.

You may assume that the majority element **always exists** in the array.

---

## Example

**Input:**  
`nums = [3, 2, 3]`

**Output:**  
`3`

---

**Input:**  
`nums = [2, 2, 1, 1, 1, 2, 2]`

**Output:**  
`2`

---

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`
- The majority element always exists.

---

## Approach

- Use the **Boyer-Moore Voting Algorithm**:
  - Initialize `count = 0` and a candidate.
  - If count drops to 0, select the current element as candidate.
  - Increment or decrement count based on match with candidate.

---

## Desired Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
*/

function majorityElement(array) {
  // edge cases: empty array
  if (!array) {
    return -1;
  }

  /*
    Boyer-Moore Voting Algorithm:
    This algorithm finds a potential majority element in linear time and constant space.
    Core idea:
    - Maintain a candidate and a counter.
    - If the counter is 0, select the current element as the new candidate.
    - If the current element equals the candidate, increment the counter.
    - Otherwise, decrement the counter.
    After one pass, the candidate is only a *potential* majority.
    A second pass is required to confirm it appears more than n / 2 times.
    */
  //Set the variables
  let count = 0;
  let candidate = -1;
  // begin first loop to get the most frequent element

  for (let i = 0; i < array.length; i++) {
    if (count == 0) {
      candidate = array[i];
      count = 1;
    } else if (array[i] == candidate) {
      count++;
    } else {
      count--;
    }
  }
  count = 0; //resetting the counter variable

  //Lets check for the frequency of our current candidate value.
  for (let i = 0; i < array.length; i++) {
    if (candidate == array[i]) {
      count++;
    }
  }
  return count > array.length / 2 ? candidate : -1;
}

console.log(majorityElement([2, 2, 1, 1, 1, 2, 2]));
console.log(majorityElement([2, 2, 1, 1, 1, 1, 1, 1, 2, 2]));
console.log(majorityElement([8]));
console.log(majorityElement([1, 2, 3, 4, 5, 6]));
console.log(majorityElement([4, 4, 4, 4]));

console.log(majorityElement([]));
