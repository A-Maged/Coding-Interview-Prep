/* 
  smallest subarray sum is >= to a given sum
*/

console.log(run([4, 2, 2, 7, 1, 2, 1, 0], 8)); // 2

function run(arr: number[], targetSum: number) {
  let smallestSubarraySize = Infinity;
  let currentWindowSum = 0;
  let windowStart = 0;

  arr.forEach((el, windowEnd) => {
    currentWindowSum += el;

    while (currentWindowSum >= targetSum) {
      smallestSubarraySize = windowEnd + 1 - windowStart;
      currentWindowSum -= arr[windowStart];

      windowStart++;
    }
  });

  return smallestSubarraySize;
}
