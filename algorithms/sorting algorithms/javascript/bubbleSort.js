const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

function bubbleSort(array) { //Not really bubble sort but a good effort in most cases
  //Code here
  for (let i = 0; i < array.length - 1; i++) {
    for (let j = i + 1; j < array.length; j++) {
      if (array[i] > array[j]) {
        let temp = array[i];
        array[i] = array[j];
        array[j] = temp;
      }
    }
  }
  return array;
}

const theRealBubbleSort = (array) => {
  for (let i = 0; i < array.length - 1; i++) {
    swapped = false; // Set a boolean flag to track swaps
    for (let j = 0; j < array.length - 1 - i; j++) {//Reduce the range after every outer loop iteration
      if (array[j] > array[j + 1]) {
        // Swap adjacent Elements
        let temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
        swapped = true;
      }
    }
    if (!swapped) {
      break;
    } //Exit if no swaps (already sorted)
  }
  return array;
};

console.log(`unsorted array : ${numbers}`);

theRealBubbleSort(numbers);

console.log(`sorted array : ${numbers}`);
