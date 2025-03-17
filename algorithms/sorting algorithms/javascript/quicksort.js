const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

function quickSort(array, left, right) {
  if (left < right) {
    let partitionIndex = partition(array, right, left, right);

    // Sort left and right
    quickSort(array, left, partitionIndex - 1);
    quickSort(array, partitionIndex + 1, right);
  }
  return array;
}

function partition(array, pivot, left, right) {
  let pivotValue = array[pivot];
  let partitionIndex = left;

  for (let i = left; i < right; i++) {
    if (array[i] < pivotValue) {
      swap(array, i, partitionIndex);
      partitionIndex++;
    }
  }
  swap(array, partitionIndex, right); // Fix: Ensure pivot is placed correctly
  return partitionIndex;
}

function swap(array, firstIndex, secondIndex) {
  [array[firstIndex], array[secondIndex]] = [
    array[secondIndex],
    array[firstIndex],
  ];
}

// Select first and last index as 2nd and 3rd parameters
console.log(quickSort(numbers, 0, numbers.length - 1));
