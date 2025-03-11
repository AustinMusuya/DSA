// Given a number N return the index value of the Fibonacci sequence, where the sequence is:

// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
// the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

//For example: fibonacciRecursive(6) should return 8

// Iterative Approach

function fibonacciIterative(n) { // Time Complexity Linear O(n)
  // edge cases
  if (n <= 0) {
    return null;
  }
  if (n == 1) {
    return 0;
  }
  let fiboArray = [0, 1];

  for (let i = 2; i <= n; i++) {
    fiboArray.push(fiboArray[i - 1] + fiboArray[i - 2]);
  }
  return fiboArray[n];
}

console.log(fibonacciIterative(6));

// Recursive Approach

function fibonacciRecursive(n) { // Time Complexity Exponential O(2^n)
  if (n < 2) {
    return n;
  }

  return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

// console.log(fibonacciRecursive(6));
