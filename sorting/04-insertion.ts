let arr = [3, 2, 9, 7, 1, 3, 0, 1];

console.log(run(arr));

function run(arr) {
  for (let i = 1; i < arr.length; i++) {
    const current = arr[i];
    let j = i;

    while (j > 0 && arr[j - 1] > current) {
      /* shift  to right*/
      arr[j] = arr[j - 1];

      j--;
    }

    arr[j] = current;
  }
  return arr;
}
