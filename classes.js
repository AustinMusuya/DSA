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

myArray.push("hi");
myArray.push("I");
myArray.push("am");
myArray.push("Austin");
myArray.push("and");
myArray.push("I");
myArray.push("love");
myArray.push("apples");

console.log(myArray);

myArray.shift();
console.log(myArray);

myArray.pop();
console.log(myArray);
