#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  // Convert the arguments to integers and store them in an array
  const numbers = process.argv.slice(2).map(Number);

  // Sort the array in descending order
  numbers.sort((a, b) => b - a);

  // Find the second largest integer
  let secondLargest = numbers[1];

  console.log(secondLargest);
}
