/* 
  smallest subarray sum is >= to a given sum
*/

console.log(run([4, 2, 2, 7, 8, 1, 2, 1, 0], 8)); // 2

function run(arr: number[], targetSum: number) {
  let smallestSubarraySize = Infinity;
  let currentWindowSum = 0;
  let windowStart = 0;

  let count = 0;

  for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
    /* increase window sum  as we progress*/
    currentWindowSum += arr[windowEnd];

    /* constraints are met? */
    while (currentWindowSum >= targetSum) {
      /* calculate current window size */
      smallestSubarraySize = windowEnd + 1 - windowStart;

      /* 
        narrow the window from tail,
        to reach smallest window possible while satisfying constraints 
      */
      currentWindowSum -= arr[windowStart];
      windowStart++;
    }
    count++;
  }

  console.log(count);

  return smallestSubarraySize;
}
