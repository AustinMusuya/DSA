// Try reverse a string of characters in javascript

let introduction = "Hi I am Austin and I rule baby!";

// Approach: we try add the string values in reverse order by looping through them
//  and storing in an array. Then we convert the array back to string and return that value.

// 1.Iterate over the values or individual values from the last to the first
// and add to an empty array.

const reverseString = (string) => {
  let firstValue = 0;
  let lastValue = string.length - 1;
  reverse = "";

  while (lastValue >= firstValue) {
    reverse += string[lastValue];
    lastValue--;
  }
  //   console.log(reverse);

  return reverse;
};

console.log(reverseString(introduction));
