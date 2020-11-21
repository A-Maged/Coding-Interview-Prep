/* 
  find the max sum subarray of a fixed size K
*/
//                  -
let arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]; // 16

console.log(run(arr, 3));

function run(arr: number[], k: number) {
  let maxSum = -Infinity;
  let currentSubarraySum = 0;
  let kMinusOne = k - 1;

  for (let i = 0; i < arr.length; i++) {
    currentSubarraySum += arr[i];

    if (i >= kMinusOne) {
      maxSum = Math.max(maxSum, currentSubarraySum);
      currentSubarraySum = currentSubarraySum - arr[i - kMinusOne];
    }
  }

  return maxSum;
}
