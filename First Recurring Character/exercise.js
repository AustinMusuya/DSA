/*
Google Question
Given an array = [2,5,1,2,3,5,1,2,4]:
It should return 2

Given an array = [2,1,1,2,3,5,1,2,4]:
It should return 1

Given an array = [2,3,4,5]:
It should return undefined */

// Brute force Approach

const firstReccuring = (input) => {
  for (let i = 0; i < input.length; i++) {
    for (let j = 0; j < i; j++) {
      if (input[i] == input[j]) {
        return input[i];
      }
    }
  }
  return undefined;
};

// console.log(firstReccuring([2, 5, 1, 2, 3, 5, 1, 2, 4]));
// console.log(firstReccuring([2, 1, 1, 2, 3, 5, 1, 2, 4]));
// console.log(firstReccuring([2, 3, 4, 5]));

// optimized approach
// Approach

const firstReccuring2 = (input) => {
  let map = {};
  for (let i = 0; i < input.length; i++) {
    if (map[input[i]] != undefined) {
      return input[i];
    } else {
      map[input[i]] = i;
    }
  }
  return undefined;
};
firstReccuring2([2, 5, 1, 2, 3, 5, 1, 2, 4]);

console.log(firstReccuring2([2, 5, 1, 2, 3, 5, 1, 2, 4]));
console.log(firstReccuring2([2, 1, 1, 2, 3, 5, 1, 2, 4]));
console.log(firstReccuring2([2, 3, 4, 5]));
