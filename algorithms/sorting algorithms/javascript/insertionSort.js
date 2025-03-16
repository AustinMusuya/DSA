const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

function insertionSort(array) {
  //Code Here
  for (let i = 1; i < array.length; i++) {
    let key = array[i];
    let j = i - 1;

    // Move elements of array[0..i-1] that are greater than key
    // one position ahead of their current position
    while (j >= 0 && array[j] > key) {
      array[j + 1] = array[j];
      j--;
    }
    array[j + 1] = key;
  }
  return array;
}

console.log(insertionSort(numbers));
