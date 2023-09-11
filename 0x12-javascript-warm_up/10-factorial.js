#!/usr/bin/node
function computeFactorial(n) {
    // Check if n is not a number (NaN)
    if (isNaN(n)) {
      console.log("Factorial of NaN is 1");
      return 1;
    }
  
    // Base case: Factorial of 0 is 1
    if (n === 0) {
      return 1;
    }
  
    // Recursive case: Compute factorial using recursion
    const factorial = n * computeFactorial(n - 1);
  
    return factorial;
  }
  
  // Get the input argument from the command line arguments
  const arg = process.argv[2];
  const n = parseInt(arg);
  
  // Compute and print the factorial
  const result = computeFactorial(n);
  console.log(`${result}`);
  