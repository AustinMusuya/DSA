/* 
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
*/

const nums = [2, 7, 11, 15];

// Optimized Approach (hashmap) Time Complexity O(n): Space Complexity O(n)

/*
We will loop through the array and store each value to a hashmap/dictionary 
in the (key:value) pair of (number:index) in the array. (i.e, 2 : 0, 7 : 1 )

A variable "complement" that is the target sum minus the array[i] i.e (9 - 2 = 7) 
will be compared to see if it is existent in the hashmap/dicitionary.

If it is then we will return an array of the two indices [0, 1] 

If not we will keep on adding values till the end of the array 
and return an empty array if we cannot find the sum pair indices

*/

const twoSum = (array, target) => {
  const numToIndex = {};
  for (let i = 0; i < array.length; i++) {
    let complement = target - array[i];
    if (complement in numToIndex) {
      return [numToIndex[complement], i];
    }
    numToIndex[array[i]] = i;
  }
  return [];
};

console.log(twoSum(nums, 9));

// Brute Force Approach nested loop Time Complexity O(n^2): Space Complexity O(1)

/* 
We will have two loops (outer and inner) where we will check to see if array[i] is equal to 
array[j]

if so then we will return the two indices of the elements in the array

Input: nums = [2,7,11,15], target = 9

*/

const twoSum2 = (array, target) => {
  for (let i = 0; i < array.length; i++) {
    for (let j = i + 1; j < array.length; j++) {
      if (array[i] + array[j] === target) {
        return [i, j];
      }
    }
  }
  return [];
};

console.log(twoSum2(nums, 9));
