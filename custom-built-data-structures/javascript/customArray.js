// Try to recreate an array using javascript classes with a few functions.

// Expected output

// {
//     length: 4,
//     data: {
//         0: value1,
//         1: value2,
//         2: value3,
//     },
// }

//  Approach:
// Create a class with constructor with field variables of length and data.
// Set the variables to 0 and an empty object/map respectively

// Push Method.
// Create a push method to add value to the data object.[length] key and increment the length variable by 1

// Pop Method.
// Create a pop method to delete the last added value at the  data.length key and decrement the length variabel by 1

// Shift Method.
// if the length is 0 then return undefined as the output
// set a variable index to the value of 0.
// loop through the elements while the last item is greater than the index, storing the data at index + 1 in data at the index then increment index by 1
// delete the last item and decrement the length by 1
// return the first item

class newArray {
  constructor() {
    this.length = 0;
    this.data = {};
  }

  push(value) {
    this.data[this.length] = value;
    this.length++;

    return this.length;
  }

  pop() {
    delete this.data[this.length - 1];
    this.length--;
  }

  shift() {
    // checkInput
    if (this.length == 0) return undefined;
    let lastItem = this.length - 1;
    let firstItem = this.data[0];
    let index = 0;

    while (index < lastItem) {
      this.data[index] = this.data[index + 1];
      index++;
    }
    delete this.data[this.length - 1];
    this.length--;

    return firstItem;
  }
}

const myArray = new newArray();

myArray.push("Hi");
myArray.push("I");
myArray.push("am");
myArray.push("Austin");
myArray.push("and");
myArray.push("I");
myArray.push("love");
myArray.push("apples");

console.log(myArray);

myArray.shift();
console.log(myArray.shift());

myArray.pop();
console.log(myArray);
