const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

function getPivot(arr, left, right) {
  let pivotValue = arr[right];
  let partitionIndex = left;

  for (let i = left; i < right; i++) {
    if (arr[i] < pivotValue) {
      [arr[i], arr[partitionIndex]] = [arr[partitionIndex], arr[i]];
      partitionIndex++;
    }
  }
  [arr[partitionIndex], arr[right]] = [arr[right], arr[partitionIndex]];
  return partitionIndex;
}

function quickSort(arr, left = 0, right = arr.length - 1) {
  if (left < right) {
    let pivot = getPivot(arr, left, right);
    quickSort(arr, left, pivot - 1);
    quickSort(arr, pivot + 1, right);
  }
  return arr;
}

// Test

console.log(quickSort(numbers));
