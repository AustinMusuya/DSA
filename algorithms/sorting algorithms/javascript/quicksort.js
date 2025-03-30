const numbersArray = [
  99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 156, 23, 77, 432, 12, 8, 234, 876, 15,
];

// Get median of three values to choose a better pivot
function getMedianOfThree(arr, left, right) {
  const mid = Math.floor((left + right) / 2);

  // Sort left, mid, and right elements
  if (arr[left] > arr[mid]) [arr[left], arr[mid]] = [arr[mid], arr[left]];
  if (arr[left] > arr[right]) [arr[left], arr[right]] = [arr[right], arr[left]];
  if (arr[mid] > arr[right]) [arr[mid], arr[right]] = [arr[right], arr[mid]];

  return mid;
}

function getPivot(arr, left, right) {
  // Use median-of-three for pivot selection
  const pivotIndex = getMedianOfThree(arr, left, right);
  const pivotValue = arr[pivotIndex];

  // Move pivot to right
  [arr[pivotIndex], arr[right]] = [arr[right], arr[pivotIndex]];

  let partitionIndex = left;

  for (let i = left; i < right; i++) {
    if (arr[i] < pivotValue) {
      [arr[i], arr[partitionIndex]] = [arr[partitionIndex], arr[i]];
      partitionIndex++;
    }
  }

  // Place pivot in correct position
  [arr[partitionIndex], arr[right]] = [arr[right], arr[partitionIndex]];
  return partitionIndex;
}

function quickSort(arr, left = 0, right = arr.length - 1) {
  // Handle empty or single-element arrays
  if (!arr || arr.length <= 1) return arr;

  if (left < right) {
    const pivot = getPivot(arr, left, right);
    quickSort(arr, left, pivot - 1);
    quickSort(arr, pivot + 1, right);
  }

  return arr;
}

// Test
console.log("Original array:", numbersArray);
console.log("Sorted array:", quickSort([...numbersArray]));
