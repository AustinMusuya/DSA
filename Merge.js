// Merge two sorted arrays into one sorted array.

let array1 = [0, 3, 4, 31];
let array2 = [3, 4, 6, 30];
let array3 = [];

// BruteForce approach

const mergeSortedArrays = (arr1, arr2) => {
  // edge cases
  // incase one of the arrays is empty

  if (arr1.length == 0) {
    return arr2;
  }

  if (arr2.length == 0) {
    return arr1;
  }
  let mergedArray = arr1.concat(arr2);

  const sortedMergedArray = mergedArray.sort((a, b) => a - b);

  return sortedMergedArray;
};

console.log(mergeSortedArrays(array1, array2));

// Optimized Approach
// Approach: check and compare the first elements in each array,
// then put the least value of the two into a new array

const mergeSortedArrays2 = (arr1, arr2) => {
  // edge cases
  // incase one of the arrays is empty

  if (!arr1) {
    return arr2;
  }

  if (!arr2) {
    return arr1;
  }

  let i = 0;
  let j = 0;
  let newArray = [];

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      newArray.push(arr1[i]);
      i++;
    } else {
      newArray.push(arr2[j]);
      j++;
    }
  }
  // Add remaining elements from arr1 (if any)
  while (i < arr1.length) {
    newArray.push(arr1[i]);
    i++;
  }

  // Add remaining elements from arr2 (if any)
  while (j < arr2.length) {
    newArray.push(arr2[j]);
    j++;
  }

  return newArray;
};

console.log(mergeSortedArrays2("x", "y"));
